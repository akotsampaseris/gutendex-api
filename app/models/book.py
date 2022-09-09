from pydantic import BaseModel
from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float

from .base_model import Base
from .book_review import BookReview

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    download_count = Column(Integer, nullable=True)
    rating = Column(Float, nullable=True)

    reviews = relationship(BookReview)
    

class BookModel(BaseModel):
    id: int
    title: str
    download_count: int = None
    rating: float = None
    
    class Config:
        orm_mode = True