import feedparser
from datetime import datetime
from models.base import db
from models.article import Article
from models.source import Source


def parse_feed(source: Source):
    """
    Parse an RSS feed and return new Article objects (not yet in DB).
    """
    feed = feedparser.parse(source.feed_url)
    new_articles = []

    for entry in feed.entries:
        if Article.query.filter_by(url=entry.link).first():
            continue  # skip duplicates

        article = Article(
            url=entry.link,
            main_image=extract_image(entry),
            author=entry.get('author', 'Unknown'),
            published_date=parse_date(entry.published_parsed),
            content=entry.get('summary', ''),
            source=source
        )
        new_articles.append(article)

    return new_articles


def parse_date(published_parsed):
    try:
        return datetime(*published_parsed[:6])
    except:
        return datetime.utcnow()


def extract_image(entry):
    # Try to extract an image from media_content or enclosure
    try:
        if "media_content" in entry:
            return entry.media_content[0].get("url", "")
        elif "media_thumbnail" in entry:
            return entry.media_thumbnail[0].get("url", "")
        elif "enclosures" in entry and entry.enclosures:
            return entry.enclosures[0].get("href", "")
    except Exception:
        pass
    return ""
