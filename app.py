from abc import ABC, abstractmethod
import csv
from utils import load_library_items, checkout_items, count_items, find_by_title


class LibraryItem(ABC):
    def __init__(self, title: str, item_id: int):
        self.title = title
        self.item_id = item_id    

    @abstractmethod
    def get_details(self, user: str) -> str:
        pass

class Book(LibraryItem):
    def __init__(self, title: str, item_id: int, author: str, page: int):
        super().__init__(title, item_id)
        self.author = author
        self.page = page

    def checkout(self, user: str) -> str:
        return f"Book '{self.title}' checked out by {user}."

class Magazine(LibraryItem):
    def __init__(self, title: str, item_id: int, issue_number: int):
        super().__init__(title, item_id)
        self.issue = issue_number

    def checkout(self, user: str) -> str:
        return f"Magazine '{self.title}' issue {self.issue} checked out by {user}."
    

# Ejemplo de uso:
if __name__ == "__main__":
    ruta = "library.csv"
    items = load_library_items(ruta)
    print("Cantidad de cada tipo:", count_items(items))
    print("Mensajes de préstamo:", checkout_items(items, "Usuario"))
    print("Resultados de búsqueda 'hobbit':", [i.title for i in find_by_title(items, "hobbit")])

