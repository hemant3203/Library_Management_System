from app.models.book import Book
from app.models.bookcopy import BookCopy
from app.models.enums import CopyStatus
from app.repositories.book_repository import BookRepository
from app.repositories.copy_repository import CopyRepository

class CatalogService:
    def __init__(self, book_repository: BookRepository, copy_repository: CopyRepository) -> None:
        self._book_repository = book_repository
        self._copy_repository = copy_repository

    def add_book(self, title:str ,author:str ,mrp:float ,copies:int)->Book:
        if copies <1:
            raise ValueError("A book must be added with at least 1 copy")
        book = self._book_repository.add(Book(id =0,title=title, author=author, mrp=mrp))
        for _ in range(copies):
            self._copy_repository.add(BookCopy(id=0,book_id=book.id, status=CopyStatus.AVAILABLE))
        return book

    def search_books(self, title:str)->list[Book]:
        return self._book_repository.search_by_title(title)

    def get_book(self, book_id:int)->Book:
        book= self._book_repository.get_by_id(book_id)
        if book is None:
            raise ValueError(f"Book with id {book_id} not found")
        return book

    def count_available_copies(self, book_id:int)->int:
        count=0
        for copy in self._copy_repository.list_by_book(book_id):
            if copy.status==CopyStatus.AVAILABLE:
                count+=1
        return count