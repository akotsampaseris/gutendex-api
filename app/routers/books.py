from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db

from app.models.book import BookModel
from app.models.book_review import BookReviewModel, BookReview

from app.services.books import BookService

router = APIRouter(
    prefix="/books",
    tags=["books"],
)

@router.get('/book/{book_id}')
def get_book_by_id(book_id: int = None) -> dict:
    book = BookService.get_book_by_id(book_id)
    book.reviews = BookService.get_book_reviews(book_id)
    
    return book


@router.post('/book/{book_id}/post-review')
def post_book_review(book_review: BookReviewModel):
    book_review = BookService.post_book_review(book_review)
    
    if not book_review:
        raise HTTPException(status_code=404, detail="Item not found")
        
    return book_review



@router.get('/search')
def search_books_by_title(title: str = None) -> list:
    books = BookService.search_book_by_title(title)
    
    return books
