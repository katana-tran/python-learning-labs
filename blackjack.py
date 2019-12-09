import random

def welcome_user():
	print("Welcome to BJ game")
	name = input("What is your name?")
	print(F"Well, hello there {name}")

def initial_deal():
	num_1 = random.randint(1,10)
	num_2 = random.randint(1,10)
	card_total = num_1 + num_2
	print(F"You received {num_1} and {num_2}")

	while card_total < 21: print(F"Your card total is {card_total}") hit_or_stay
	= input("Would you like to draw again? y/n") if hit_or_stay == "y":
	card_total += random.randint(1,10)


	print(F"Your card total is {card_total}! Sorry, you've exceeded 21. You lose.")

def run_game():
	welcome_user()
	initial_deal()

run_game()