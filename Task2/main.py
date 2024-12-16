from abc import ABC, abstractmethod
from dataclasses import dataclass
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class Book:
    title: str
    author: str
    year: str

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self._books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)
        logger.info(f"Added book: {book}")

    def remove_book(self, title: str) -> None:
        initial_length = len(self._books)
        self._books = [book for book in self._books if book.title != title]
        if len(self._books) < initial_length:
            logger.info(f"Removed book with title: {title}")
        else:
            logger.info(f"Book with title '{title}' not found")

    def show_books(self) -> None:
        if not self._books:
            logger.info("No books in library")
            return
        logger.info("Library contents:")
        for book in self._books:
            logger.info(str(book))


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self._library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title=title, author=author, year=year)
        self._library.add_book(book)

    def remove_book(self, title: str) -> None:
        self._library.remove_book(title)

    def show_books(self) -> None:
        self._library.show_books()


def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    logger.info("Welcome to the Library Management System!")

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)

            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)

            case "show":
                manager.show_books()

            case "exit":
                logger.info("Goodbye!")
                break

            case _:
                logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
