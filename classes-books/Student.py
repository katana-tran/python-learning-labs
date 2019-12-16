class Student:
	def __init__(self, name, favorite_book="No favorite"):
		self.name = name
		self.favorite_book = favorite_book

	def assign_new_favorite_book(self, new_book):
		self.favorite_book = new_book
		
