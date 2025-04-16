from datetime import datetime

class BaseParser:
    def __init__(self, entry, source):
        self.entry = entry
        self.source = source

    def parse(self):
        return {
            "url": self.entry.link,
            "title": self.entry.title,
            "author": self.get_author(),
            "content": self.get_content(),
            "image": self.get_image(),
            "published": self.get_published()
        }

    def get_author(self):
        return self.entry.get("author", "Unknown")

    def get_content(self):
        return self.entry.get("summary", "")

    def get_image(self):
        return ""

    def get_published(self):
        try:
            return datetime(*self.entry.published_parsed[:6])
        except:
            return datetime.utcnow()
