def fizzbuzz(number):
	if number % 3 == 0 and number % 5 == 0:
		print("FizzBuzz")
	elif number % 3 == 0:
		print("fizz")
	elif number % 5 == 0:
		print("buzz")
	else: 
		print("None")
		return None

fizzbuzz(3)
fizzbuzz(5)
fizzbuzz(15)
fizzbuzz(4)