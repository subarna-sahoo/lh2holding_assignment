from flask import Blueprint, jsonify, request
from models.article import Article
from models.source import Source
from models.base import db
from sqlalchemy import desc
from datetime import datetime

bp = Blueprint('articles', __name__, url_prefix='/articles')

@bp.route('/', methods=['GET'])
def get_articles():
    date_str = request.args.get('date')  # Optional: ?date=2025-04-16
    source_id = request.args.get('source_id')  # Optional: ?source_id=1

    query = Article.query

    if date_str:
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            query = query.filter(db.func.date(Article.published_date) == date)
        except:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

    if source_id:
        query = query.filter(Article.source_id == source_id)

    articles = query.order_by(desc(Article.published_date)).limit(50).all()

    return jsonify([
        {
            "id": a.id,
            "url": a.url,
            "image": a.main_image,
            "author": a.author,
            "date": a.published_date.isoformat() if a.published_date else None,
            "summary": a.summary,
            "source": a.source.name if a.source else None
        }
        for a in articles
    ])
