from fastapi import Body, FastAPI

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


@app.get('/books/')
async def get_books_by_category(category: str):
    res = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            res.append(book)
    return res


@app.get('/books/{book_author}')
async def read_by_author_category(book_author: str, category: str):
    res = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            return book
    return 'Book with matching author and category not found'


@app.get('/books/{book_title}')
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return 'Book with matching title not found'


@app.post('/books')
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put('/books')
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
            return updated_book
