# primerparcial_programaciondos
Clases abstractas y herencia: sistema de biblioteca


Instituto Técnico Superior Córdoba
Tecnicatura Superior en Desarrollo de Software
Asignatura: Programación II

Primer parcial

Subir el código a github y compartir la url en el aula virtual de la materia.

Temas
1. Clases abstractas e herencia: sistema de biblioteca
• Define clase abstracta LibraryItem con:
• Atributos: title: str, item_id: int.
• Método abstracto checkout(self, user: str) -> str que simule
prestar el ítem (retorna mensaje).
• Subclases:
• Book: recibe además author: str, pages: int. checkout retorna
"Book '{title}' checked out by {user}.".
• Magazine: recibe además issue_number: int. checkout retorna
"Magazine '{title}' issue {issue_number} checked out
by {user}.".
• Validar en constructores: cadenas no vacías, IDs y números positivos adecuados.
3. Manejo de CSV
• Archivo library.csv, cada línea:
• Tipo (book o magazine), título, id, y luego:
• Para book: autor, número de páginas.
• Para magazine: número de issue.
• Escribe load_library_items(path: str) -> list[LibraryItem],
ignorando o registrando errores.
4. Reporte y operaciones
• Función checkout_items(items: list[LibraryItem], user: str)
-> list[str] que recorra la lista y aplique checkout(user) en cada uno,
devolviendo mensajes.
• Función count_items(items: list[LibraryItem]) -> dict con
conteo por tipo: {"book": X, "magazine": Y}.
• Función find_by_title(items: list[LibraryItem], keyword:
str) -> list[LibraryItem] que devuelva los cuyo título contenga (caseinsensitive) la palabra clave.
5. Pruebas con unittest
• Probar constructores válidos e inválidos.
• Probar checkout para cada subclase.
• Probar load_library_items con CSV temporal.
• Probar funciones de reporte (checkout_items, count_items,
find_by_title).
