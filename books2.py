from fastapi import Body, FastAPI

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


BOOKS = [
    Book(1, 'Argument of Kings', 'Joe Abercrombie', 'Lovely fantasy book', 5),
    Book(2, 'Harry Potter', 'J K Rowling', 'Another magical childhood book', 4),
    Book(3, 'New Fantasy Book', 'Joe Abercrombie', 'Another one by this guy', 3)
]


@app.get('/books')
async def read_all_books():
    return BOOKS


@app.post('/books')
async def create_book(req=Body()):
    BOOKS.append(req)
