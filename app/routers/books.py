from fastapi import APIRouter, Body
from fastapi_sqlalchemy import db

from app.models.book import BookModel, Book
from app.models.book_review import BookReviewModel, BookReview

from app.services.book import BookService
from app.services.gutendex import GutendexService

router = APIRouter(
    prefix="/books",
    tags=["books"],
)

@router.get('/')
def get_books() -> dict:
    books = db.session.query(Book).all()
    return books


@router.get('/reviews')
def get_book_reviews() -> dict:
    book = db.session.query(Book).first()

    return book.reviews


@router.get('/book/{id}')
def get_book_by_id(id: int = None) -> dict:
    book = GutendexService.get_book_by_id(id)
    
    return book


@router.post('/book/{id}/post-review')
def post_book_review(book_review: BookReviewModel) -> dict:
    book = GutendexService.get_book_by_id(book_review.book_id)
    
    db.session.add(
        BookReview(
            book_id = book_review.book_id, 
            rating=book_review.rating, 
            review=book_review.review
        )
    )

    db.session.commit()

    return book_review

    

@router.get('/search')
def search_books_by_title(title: str = None) -> list:
    return GutendexService.search_book_by_title(title)

