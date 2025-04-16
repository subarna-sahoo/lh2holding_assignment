from services.parser_factory import get_parser

def parse_feed(source):
    import feedparser
    from models.article import Article

    feed = feedparser.parse(source.feed_url)
    new_articles = []

    for entry in feed.entries:
        if Article.query.filter_by(url=entry.link).first():
            continue

        parser = get_parser(source, entry)
        parsed = parser.parse()

        article = Article(
            url=parsed["url"],
            # title=parsed["title"], # We are also getting title from the xml
            author=parsed["author"],
            main_image=parsed["image"],
            content=parsed["content"],
            published_date=parsed["published"],
            source=source
        )

        new_articles.append(article)

    return new_articles
