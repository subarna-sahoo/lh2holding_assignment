from flask import Blueprint, request, jsonify
from models.source import Source
from models.base import db

bp = Blueprint("sources", __name__, url_prefix="/sources")

@bp.route("/", methods=["GET"])
def get_sources():
    sources = Source.query.all()
    return jsonify([
        {
            "id": s.id,
            "name": s.name,
            "feed_url": s.feed_url
        } for s in sources
    ])

@bp.route("/", methods=["POST"])
def add_source():
    data = request.get_json()

    if not data or "name" not in data or "feed_url" not in data:
        return jsonify({"error": "Missing 'name' or 'feed_url'"}), 400

    existing = Source.query.filter_by(feed_url=data["feed_url"]).first()
    if existing:
        return jsonify({"error": "Source already exists"}), 409

    source = Source(name=data["name"], feed_url=data["feed_url"])
    db.session.add(source)
    db.session.commit()

    return jsonify({
        "id": source.id,
        "name": source.name,
        "feed_url": source.feed_url
    }), 201
