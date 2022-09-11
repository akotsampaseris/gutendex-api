from pydantic import BaseModel
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Column, Integer, String, Float, DateTime

Base = declarative_base()

class BookReview(Base):
    __tablename__ = 'book_reviews'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    rating = Column(Float)
    comment = Column(String)
    created_at = Column(DateTime)

    
class BookReviewModel(BaseModel):
    book_id: int
    rating: float
    comment: str = None 
    created_at: datetime = None
    
    class Config:
        orm_mode = True