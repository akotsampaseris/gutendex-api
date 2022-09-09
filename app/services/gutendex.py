import requests

from app.models.book import BookModel


class GutendexService():
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
    def search_book_by_title(cls, title: str = None) -> list:
        if not title:
            return []
        
        url = cls.base_url
        response = requests.get(url, params={"search": title.replace(' ', '%20')})
        results = response.json()['results']        
        
        return [BookModel(**result) for result in results]

