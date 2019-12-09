array_of_numbers = [2,4,6,8]

def square_number(number):
	return number * number

def squared_numbers(array_of_numbers):
	result = map(square_number, array_of_numbers)
	print(list(result))

squared_numbers(array_of_numbers)

def squared_numbers(array_of_numbers):
	arr = []
	for number in array_of_numbers:
		squared = number*number
		arr.append(squared)
	print(arr)

squared_numbers(array_of_numbers)