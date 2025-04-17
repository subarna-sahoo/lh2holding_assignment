from services.parser_factory import get_parser


def parse_feed(source):
    """Return list[dict] – each dict ready for Article(**d)."""
    return get_parser(source).parse_feed()