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
                return  # Already summarized or invalid

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
            new_articles = parse_feed(source)
            for article in new_articles:
                db.session.add(article)
                db.session.flush()  # get article.id before commit
                summarize_article.delay(article.id)
            db.session.commit()
