from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title 1', 'author': 'Author 1', 'category': 'science'},
    {'title': 'Title 2', 'author': 'Author 2', 'category': 'science'},
    {'title': 'Title 3', 'author': 'Author 3', 'category': 'history'},
    {'title': 'Title 4', 'author': 'Author 4', 'category': 'math'},
    {'title': 'Title 5', 'author': 'Author 5', 'category': 'math'},
    {'title': 'Title 6', 'author': 'Author 2', 'category': 'math'},
]


@app.get('/books')
async def read_all_books():
    return BOOKS


@app.get('/books/{book_title}')
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return 'Book with matching title not found'
