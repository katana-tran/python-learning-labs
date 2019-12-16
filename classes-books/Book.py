class Book:
	def __init__(self, title, author, completed_pages, total_pages):
		self.title = title
		self.author = author
		self.completed_pages = completed_pages
		self.total_pages = total_pages

	def turn_page(self):
		uncompleted_pages = self.total_pages - self.completed_pages
		if uncompleted_pages > 0:
			self.completed_pages += 1
			print(f"You read a page. Currently you've read {self.completed_pages} of {self.total_pages} pages.")
		else:
			while True:
				answer = input("You've already finished this book. Would you like to restart? y/n") 
				if answer == "y":
					self.completed_pages = 0
					print(f"Now resetted to {self.completed_pages}")
					break
				elif answer == "n":
					print("Terminating process.")
					break
				else:
					print("You didn't pick yes(y) or no(n).")

	def complete_homework(self):
		uncompleted_pages = self.total_pages - self.completed_pages
		if uncompleted_pages < 50:
			self.completed_pages += uncompleted_pages
			print(f"You've read {uncompleted_pages} more pages for homework and finished the novel.")
		else:
			self.completed_pages += 50
			print(f"You've read 50 more pages for homework. Currently at {self.completed_pages} of {self.total_pages}.")

	