from abc import ABC, abstractmethod
from datetime import datetime


class BaseParser(ABC):
    """Abstract superclass for all feed‑specific parsers."""

    def __init__(self, source):
        self.source = source
    
    @abstractmethod
    def url(self, entry):
        pass

    @abstractmethod
    def author(self, entry):
        pass
    
    @abstractmethod
    def image(self, entry):
        pass

    @abstractmethod
    def content(self, entry):
        pass
    
    @abstractmethod
    def published_date(self, entry):
        pass

    @abstractmethod
    def parse_feed(self):
        pass