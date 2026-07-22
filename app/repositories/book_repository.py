from abc import ABC, abstractmethod
from typing import Optional

from app.models.book import Book

class BookRepository(ABC):

    @abstractmethod
    def add(self, book :Book)->Book:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, book_id:int)->Optional[Book]:
        raise NotImplementedError

    @abstractmethod
    def list_all(self)->list[Book]:
        raise NotImplementedError

    @abstractmethod
    def search_by_title(self, title:str)->list[Book]:
        raise NotImplementedError


class InMemoryBookRepository(BookRepository):

    def __init__(self)-> None:
        self._books:dict[int,Book] = {}
        self._next_id:int =1

    def add(self,book :Book)->Book:
        book.id=self._next_id
        self._books[book.id]=book
        self._next_id+=1
        return book

    def get_by_id(self, book_id:int)->Optional[Book]:
        return self._books.get(book_id)

    def list_all(self)->list[Book]:
        return list(self._books.values())

    def search_by_title(self, title:str)->list[Book]:
        results: list[Book]=[]
        for book in self._books.values():
            if title.lower() in book.title.lower():
                results.append(book)
        return results