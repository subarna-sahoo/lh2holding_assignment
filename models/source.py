from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import db


class Source(db.Model):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    feed_url = Column(String(1024), unique=True, nullable=False)

    articles = relationship("Article", back_populates="source", cascade="all, delete")
