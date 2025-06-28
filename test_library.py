import unittest
from library_item import Book, Magazine
from utils import checkout_items, count_items, find_by_title, load_library_items
import tempfile
import os

class TestLibrary(unittest.TestCase):
    def test_checkout_book(self):
        book = Book("Cien Años de Soledad", 1, "Gabriel Garcia Márquez", 417)
        result = book.checkout("Alice")
        self.assertEqual(result, "Book 'Cien Años de Soledad' checked out by Alice.")

    def test_checkout_magazine(self):
        mag = Magazine("National Geographic", 2, 120)
        result = mag.checkout("Bob")
        self.assertEqual(result, "Magazine 'National Geographic' issue 120 checked out by Bob.")

    def test_invalid_book(self):
        with self.assertRaises(ValueError):
            Book("", 1, "Autor", 100)
        with self.assertRaises(ValueError):
            Book("Titulo", -1, "Autor", 100)
        with self.assertRaises(ValueError):
            Book("Titulo", 1, "", 100)
        with self.assertRaises(ValueError):
            Book("Titulo", 1, "Autor", 0)

    def test_invalid_magazine(self):
        with self.assertRaises(ValueError):
            Magazine("", 2, 10)
        with self.assertRaises(ValueError):
            Magazine("Revista", -2, 10)
        with self.assertRaises(ValueError):
            Magazine("Revista", 2, 0)

    def test_checkout_items(self):
        items = [
            Book("Libro1", 1, "Autor1", 100),
            Magazine("Revista1", 2, 5)
        ]
        mensajes = checkout_items(items, "Carlos")
        self.assertEqual(mensajes, [
            "Book 'Libro1' checked out by Carlos.",
            "Magazine 'Revista1' issue 5 checked out by Carlos."
        ])

    def test_count_items(self):
        items = [
            Book("Libro1", 1, "Autor1", 100),
            Magazine("Revista1", 2, 5),
            Book("Libro2", 3, "Autor2", 200)
        ]
        conteo = count_items(items)
        self.assertEqual(conteo, {"book": 2, "magazine": 1})

    def test_find_by_title(self):
        items = [
            Book("El Principito", 1, "Saint-Exupéry", 96),
            Magazine("Ciencia Hoy", 2, 33),
            Book("Principios de Física", 3, "Serway", 1200)
        ]
        encontrados = find_by_title(items, "prin")
        self.assertEqual(len(encontrados), 2)
        self.assertTrue(any("El Principito" in i.title for i in encontrados))
        self.assertTrue(any("Principios de Física" in i.title for i in encontrados))

    def test_load_library_items(self):
        contenido = (
            "book,El Hobbit,1,J.R.R. Tolkien,310\n"
            "magazine,Investigación y Ciencia,2,45\n"
            "book,Sin Autor,3,,200\n"
            "magazine,Revista Inválida,-4,10\n"
        )
        with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as tmp:
            tmp.write(contenido)
            tmp_path = tmp.name
        items = load_library_items(tmp_path)
        os.remove(tmp_path)
        self.assertEqual(len(items), 2)
        self.assertIsInstance(items[0], Book)
        self.assertIsInstance(items[1], Magazine)

if __name__ == "__main__":
    unittest.main()