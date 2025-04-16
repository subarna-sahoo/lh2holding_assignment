from flask import Blueprint, jsonify, request
from models.article import Article
from models.source import Source
from models.base import db
from sqlalchemy import desc
from datetime import datetime
from utils.tasks import fetch_and_queue_articles  # for fetch-now

bp = Blueprint('articles', __name__, url_prefix='/articles')



@bp.route("/", methods=["GET"])
def get_articles():
    date_str = request.args.get("date")
    source_id = request.args.get("source_id")
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    query = Article.query

    if date_str:
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            query = query.filter(db.func.date(Article.published_date) == date)
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

    if source_id:
        query = query.filter(Article.source_id == source_id)

    total = query.count()
    articles = query.order_by(desc(Article.published_date)) \
                    .offset((page - 1) * limit) \
                    .limit(limit) \
                    .all()

    return jsonify({
        "meta": {
            "page": page,
            "limit": limit,
            "total": total,
            "pages": (total + limit - 1) // limit  # ceiling division
        },
        "data": [
            {
                "id": a.id,
                "url": a.url,
                "image": a.main_image,
                "author": a.author,
                "content": a.content,
                "date": a.published_date.isoformat() if a.published_date else None,
                "summary": a.summary,
                "source": a.source.name if a.source else None
            } for a in articles
        ]
    })


@bp.route("/fetch-now", methods=["POST"])
def fetch_now():
    fetch_and_queue_articles.delay()
    return jsonify({"status": "Feed fetch task enqueued"}), 202