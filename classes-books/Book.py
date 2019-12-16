class Book:
	def __init__(self, title, author, completed_pages, total_pages):
		self.title = title
		self.author = author
		self.completed_pages = completed_pages
		self.total_pages = total_pages

	def turn_page(self):
		self.completed_pages += 1
		print("You're reading quite fast!")
		print(f"Currently you've read {self.completed_pages} of {self.total_pages} pages.")

	def complete_homework(self):
		self.completed_pages += 50
		print(f"You've read 50 more pages for homework. Currently at {self.completed_pages} of {self.total_pages}.")
