from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)  # Rating can only be 0 to 5


BOOKS = [
    Book(1, 'Argument of Kings', 'Joe Abercrombie', 'Lovely fantasy book', 5),
    Book(2, 'Harry Potter', 'J K Rowling', 'Another magical childhood book', 4),
    Book(3, 'New Fantasy Book', 'Joe Abercrombie', 'Another one by this guy', 3)
]


@app.get('/books')
async def read_all_books():
    return BOOKS


@app.post('/books')
async def create_book(req: BookRequest):
    new_book = Book(**req.model_dump())
    BOOKS.append(new_book)
