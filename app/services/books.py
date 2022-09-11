import requests
from fastapi_sqlalchemy import db
from datetime import datetime

from app.models.book import BookModel
from app.models.book_review import BookReviewModel, BookReview


class BookService():
    base_url = "https://gutendex.com/books"

    @classmethod
    def get_book_by_id(cls, id: int = None):
        if not id:
            return None
        
        url = '/'.join([cls.base_url, str(id)])
        response = requests.get(url)
        result = response.json()
        
        return BookModel(**result)


    @classmethod
    def get_book_reviews(cls, book_id: int = None):
        results = db.session.query(BookReview).\
            filter_by(book_id=book_id).all()
        
        return results


    @classmethod
    def search_book_by_title(cls, title: str = None) -> list:
        if not title:
            return []
        
        url = cls.base_url
        response = requests.get(url, params={"search": title.replace(' ', '%20')})
        results = response.json()['results']        
        
        return [BookModel(**result) for result in results]
   
    
    @classmethod
    def post_book_review(cls, book_review: BookReviewModel = None):        
        try:
            db.session.add(
                BookReview(
                    book_id = book_review.book_id, 
                    rating=book_review.rating, 
                    comment=book_review.comment,
                    created_at=datetime.now()
                )
            )
            db.session.commit()
            
            return book_review            
        except ValueError:
            raise ValueError
            

