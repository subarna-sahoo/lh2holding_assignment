from services.parser_factory import get_parser


def parse_feed(source):
    parser = get_parser(source)  # ✅ Returns the correct concrete class
    return parser.parse_feed()