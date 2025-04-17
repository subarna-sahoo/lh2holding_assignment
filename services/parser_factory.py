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


from services.parsers.aviation_parser import AviationParser
from services.parsers.air_land_sea_parser import AirLandSeaParser


def get_parser(source):
    name = source.name.lower()

    if "aviation" in name:
        return AviationParser(source)

    elif "air land & sea defense" in name:
        return AirLandSeaParser(source)

    else:
        raise ValueError(f"❌ No parser found for source: {source.name}")
    
