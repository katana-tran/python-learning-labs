from Book import Book
from Student import Student

her_smoke = Book("Her Smoke Rose Up Forever", "James Tiptree", 40, 100)
caves_of_steel = Book("Caves of Steel", "Isaac Asimov", 0, 100)
katana = Student("Katana", her_smoke)

print(her_smoke.completed_pages)
her_smoke.complete_homework()
print(her_smoke.completed_pages)

print(katana.favorite_book.title)
katana.assign_new_favorite_book(caves_of_steel)
print(katana.favorite_book.title)