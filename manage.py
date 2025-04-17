# manage.py
from flask.cli import FlaskGroup
from app import create_app
from models.base import db
from models.source import Source

app = create_app()
cli = FlaskGroup(app)

@cli.command("seed_sources")
def seed_sources():
    sources = [
        Source(name="Aviation", feed_url="https://www.inoreader.com/stream/user/1003839719/tag/Aviation"),
        Source(name="Air Land & Sea Defense", feed_url="https://www.inoreader.com/stream/user/1003839719/tag/Air%2C%20Land%20%26%20Sea%20Defense")
    ]
    for src in sources:
        if not Source.query.filter_by(feed_url=src.feed_url).first():
            db.session.add(src)
    db.session.commit()
    print("✅ Seeded source data.")

if __name__ == "__main__":
    cli()
