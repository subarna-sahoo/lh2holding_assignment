import feedparser, html
from bs4 import BeautifulSoup
from services.parsers.base import BaseParser


class AirLandSeaParser(BaseParser):
    """Custom rules for 'Air, Land & Sea Defense' feed."""

    def url(self, entry):
        return entry.get("link", "")

    def author(self, entry):
        return entry.get("author", "Unknown")

    def image(self, entry):
        return self._extract_image_url(entry.get("summary", ""))

    def content(self, entry):
        return entry.get("summary", "")

    def published_date(self, entry):
        return entry.get("published", "")

    def parse_feed(self):
        feed = feedparser.parse(self.source.feed_url)
        rows = []
        print(f"Parsing feed: {feed}")
 
        for e in feed.entries:
            rows.append(
                {
                    "url": self.url(e),
                    "author": self.author(e),
                    "main_image": self.image(e),
                    "content": self.content(e),
                    "published_date": self.published_date(e),
                }
            )

        return rows


    def _extract_image_url(self, summary):
        soup = BeautifulSoup(summary, "html.parser")
        img = soup.find("img")
        return img["src"] if img else ""
