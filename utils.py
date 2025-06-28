import csv
from library_item import Book, Magazine, LibraryItem

def load_library_items(path: str) -> list[LibraryItem]:
    items = []
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                item_type = row[0].strip().lower()
                title = row[1].strip()
                item_id = int(row[2])
                if item_type == 'book':
                    author = row[3].strip()
                    pages = int(row[4])
                    items.append(Book(title, item_id, author, pages))
                elif item_type == 'magazine':
                    issue_number = int(row[3])
                    items.append(Magazine(title, item_id, issue_number))
            except Exception:
                continue
    return items

def checkout_items(items: list[LibraryItem], user: str) -> list[str]:
    return [item.checkout(user) for item in items]

def count_items(items: list[LibraryItem]) -> dict:
    conteo = {"book": 0, "magazine": 0}
    for item in items:
        if isinstance(item, Book):
            conteo["book"] += 1
        elif isinstance(item, Magazine):
            conteo["magazine"] += 1
    return conteo

def find_by_title(items: list[LibraryItem], keyword: str) -> list[LibraryItem]:
    keyword = keyword.lower()
    return [item for item in items if keyword in item.title.lower()]