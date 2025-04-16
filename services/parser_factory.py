import re
from services.parsers.base import BaseParser

import re
from services.parsers.base import BaseParser

def get_parser(source, entry):
    parser = BaseParser(entry, source)
    name = source.name.lower().replace(" ", "")

    if name == "aviation":
        def get_author():
            return entry.get("dc_creator") or entry.get("author", "Unknown")

        def get_image():
            try:
                from bs4 import BeautifulSoup

                if "description" in entry:
                    soup = BeautifulSoup(entry.description, "html.parser")
                    img = soup.find("img")
                    if img and img.get("src"):
                        return img["src"]
            except Exception as e:
                print("Image parse error:", e)

            return ""

        def get_content():
            # Remove <a> tag and keep plain content
            try:
                return re.sub(r'<a.*?</a>', '', entry.description, flags=re.DOTALL).strip()
            except Exception:
                return entry.get("summary", "")

        # Override parser methods for this source
        parser.get_author = get_author
        parser.get_image = get_image
        parser.get_content = get_content

    return parser
