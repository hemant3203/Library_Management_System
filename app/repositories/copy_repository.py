from abc import ABC, abstractmethod
from typing import Optional

from app.models.bookcopy import BookCopy
from app.models.enums import CopyStatus


class CopyRepository(ABC):

    @abstractmethod
    def add(self, copy: BookCopy) -> BookCopy:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, copy_id: int) -> Optional[BookCopy]:
        raise NotImplementedError

    @abstractmethod
    def list_by_book(self, book_id: int) -> list[BookCopy]:
        raise NotImplementedError

    @abstractmethod
    def find_available(self, book_id: int) -> Optional[BookCopy]:
        raise NotImplementedError


class InMemoryCopyRepository(CopyRepository):

    def __init__(self) -> None:        
        self._copies: dict[int, BookCopy] = {}
        self._next_id: int = 1

    def add(self, copy: BookCopy) -> BookCopy:
        copy.id = self._next_id
        self._copies[copy.id] = copy
        self._next_id += 1
        return copy

    def get_by_id(self, copy_id: int) -> Optional[BookCopy]:
        return self._copies.get(copy_id)

    def list_by_book(self, book_id: int) -> list[BookCopy]:
        # YOUR PART 1 — basket pattern (like search_by_title):
        # empty list → loop values → if copy.book_id matches → append → return
        books: list[BookCopy] = []
        for copy in self._copies.values():
            if copy.book_id == book_id:
                books.append(copy)
        return books

    def find_available(self, book_id: int) -> Optional[BookCopy]:
        # YOUR PART 2 — early return (like get_by_email), but the if checks
        # TWO conditions joined with `and`:
        #   right book?  AND  status == CopyStatus.AVAILABLE
        # loop → if both true → return copy ; after loop → return None
        for copy in self._copies.values():
            if copy.book_id == book_id and copy.status == CopyStatus.AVAILABLE:
                return copy
        return None
