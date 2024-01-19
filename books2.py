from typing import Optional
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
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)  # Rating can only be 0 to 5

    class Config:
        # Example schema specifies the example value for a schema in documentation
        json_schema_extra = {
            'example': {
                'title': 'A new book hard coded as default input',
                'author': 'Default author as per config',
                'description': 'This is a description for a book',
                'rating': 4
            }
        }


BOOKS = [
    Book(1, 'Argument of Kings', 'Joe Abercrombie', 'Lovely fantasy book', 5),
    Book(2, 'Harry Potter', 'J K Rowling', 'Another magical childhood book', 4),
    Book(3, 'New Fantasy Book', 'Joe Abercrombie', 'Another one by this guy', 3)
]


@app.get('/books')
async def read_all_books():
    return BOOKS


@app.get('/books/{book_id}')
async def read_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book


@app.get('/books/')
async def read_book_by_rating(book_rating: int):
    res = []
    for book in BOOKS:
        if book.rating == book_rating:
            res.append(book)
    return res


@app.post('/books')
async def create_book(req: BookRequest):
    new_book = Book(**req.model_dump())
    BOOKS.append(get_book_id(new_book))

    return new_book


def get_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1

    return book


@app.put('/books/{book_id}')
async def update_book(book_id: int, book_req: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            book_req.id = book_id
            BOOKS[i] = book_req
    return book_req


@app.delete('/books/{book_id}')
async def delete_book(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            res = BOOKS.pop(i)
            return res
