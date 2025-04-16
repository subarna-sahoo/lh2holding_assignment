from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base import db


class Article(db.Model):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    url = Column(String(1024), unique=True, nullable=False)
    main_image = Column(String(1024))
    author = Column(String(255))
    published_date = Column(DateTime)
    content = Column(Text)
    summary = Column(Text)

    source_id = Column(Integer, ForeignKey("sources.id"))
    source = relationship("Source", back_populates="articles")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
