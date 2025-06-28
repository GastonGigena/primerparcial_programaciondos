from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title: str, item_id: int):
        if not title or not isinstance(title, str):
            raise ValueError("El título debe ser una cadena no vacía.")
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("El ID debe ser un entero positivo.")
        self.title = title
        self.item_id = item_id

    @abstractmethod
    def checkout(self, user: str) -> str:
        pass

class Book(LibraryItem):
    def __init__(self, title: str, item_id: int, author: str, pages: int):
        super().__init__(title, item_id)
        if not author or not isinstance(author, str):
            raise ValueError("El autor debe ser una cadena no vacía.")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("El número de páginas debe ser un entero positivo.")
        self.author = author
        self.pages = pages

    def checkout(self, user: str) -> str:
        return f"Book '{self.title}' checked out by {user}."

class Magazine(LibraryItem):
    def __init__(self, title: str, item_id: int, issue_number: int):
        super().__init__(title, item_id)
        if not isinstance(issue_number, int) or issue_number <= 0:
            raise ValueError("El número de issue debe ser un entero positivo.")
        self.issue_number = issue_number

    def checkout(self, user: str) -> str:
        return f"Magazine '{self.title}' issue {self.issue_number} checked out by {user}."