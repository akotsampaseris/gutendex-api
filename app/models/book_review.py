from pydantic import BaseModel
from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String, Float

from .base_model import Base


class BookReview(Base):
    __tablename__ = 'book_reviews'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    rating = Column(Float)
    review = Column(String)

    
class BookReviewModel(BaseModel):
    book_id: int
    rating: float
    review: str
    
    class Config:
        orm_mode = True