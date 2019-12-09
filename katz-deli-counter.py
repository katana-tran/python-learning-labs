katz_deli = [] 

def line(array):
	if len(array) == 0:
		print("The line is currently empty.")
	else: 
		print("Current line is as follows:")
		counter = 1
		for i in array:
			print(F"{counter}: {i}")
			counter += 1


def take_a_number(current_line, new_name):
	current_line.append(new_name)
	print(F"{new_name}, you're number {len(current_line)} in line.")

def now_serving(current_line):
	name = current_line.pop(0)
	print(F"Now serving: {name}")



take_a_number(katz_deli, "Ada") #=> Welcome, Ada. You are number 1 in line.
take_a_number(katz_deli, "Grace") #=> Welcome, Grace. You are number 2 in line.
take_a_number(katz_deli, "Kent") #=> Welcome, Kent. You are number 3 in line.
line(katz_deli) #=> "The line is currently: 1. Ada 2. Grace 3. Kent"
now_serving(katz_deli) #=> "Currently serving Ada."
line(katz_deli) #=> "The line is currently: 1. Grace 2. Kent"
take_a_number(katz_deli, "Matz") #=> Welcome, Matz. You are number 3 in line.
line(katz_deli) #=> "The line is currently: 1. Grace 2. Kent 3. Matz"
now_serving(katz_deli) #=> "Currently serving Grace."