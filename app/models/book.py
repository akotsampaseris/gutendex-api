from pydantic import BaseModel   

class BookModel(BaseModel):
    id: int
    title: str
    authors: list
    languages: list
    download_count: int = None
    rating: float = None
    reviews: list = None
    
    class Config:
        orm_mode = True