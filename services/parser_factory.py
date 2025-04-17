from services.parsers.base import BaseParser
from services.parsers import AviationParser, AirLandSeaParser

_REGISTRY = {
    "aviation":                AviationParser,
    "air,land&seadefense":     AirLandSeaParser,
}


def get_parser(source):
    key = source.name.lower().replace(" ", "")
    cls = _REGISTRY.get(key, BaseParser)
    return cls(source)
