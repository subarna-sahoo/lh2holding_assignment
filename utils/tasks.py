from utils.celery_app import celery
from utils.summarizer import summarize_text
from models.article import Article
from models.base import db
from app import create_app
from models.source import Source
from services.rss_parser import parse_feed

@celery.task(bind=True, max_retries=3)
def summarize_article(self, article_id):
    app = create_app()
    with app.app_context():
        try:
            article = Article.query.get(article_id)
            if not article or article.summary:
                return  # Already summarized or not found

            summary = summarize_text(article.content)
            article.summary = summary
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise self.retry(exc=e, countdown=10)


@celery.task
def fetch_and_queue_articles():
    app = create_app()
    with app.app_context():
        sources = Source.query.all()

        for source in sources:
            try:
                new_articles = parse_feed(source)
            except Exception as e:
                print(f"❌ Failed to parse feed for {source.name}: {e}")
                continue

            for article_data in new_articles:
                try:
                    # Ensure uniqueness (avoid inserting same article)
                    existing = Article.query.filter_by(url=article_data["url"]).first()
                    if existing:
                        continue

                    article = Article(**article_data, source_id=source.id)
                    db.session.add(article)
                    db.session.flush()  # Ensures article.id is available

                    summarize_article.delay(article.id)
                except Exception as e:
                    db.session.rollback()
                    print(f"⚠️ Failed to insert article from {source.name}: {e}")

            db.session.commit()
