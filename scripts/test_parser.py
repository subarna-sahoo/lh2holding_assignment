import sys
import os
sys.path.append(os.path.abspath("."))  # add /app to PYTHONPATH

from app import create_app
from models.source import Source
from services.parser_factory import get_parser
import feedparser


app = create_app()

with app.app_context():
    # Simulate an existing source
    source = Source(
        name="Aviation",
        feed_url="https://www.inoreader.com/stream/user/1003839719/tag/Aviation"
    )

    feed = feedparser.parse(source.feed_url)

    print(f"✅ Found {len(feed.entries)} entries")

    if not feed.entries:
        print("⚠️ No entries found. Feed might be down.")
        exit()

    entry = feed.entries[0]  # Pick first entry for test
    parser = get_parser(source, entry)
    parsed = parser.parse()

    print("🧪 Parsed result:")
    print(parsed)
