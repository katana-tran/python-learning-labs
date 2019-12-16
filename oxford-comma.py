animal_string = "hippo,penguin,bob,sally"

def oxford_comma(string):
	string_array = string.split(',')
	print(string_array)
	if len(string_array) <= 2:
		string_array.insert(1, "and")
		new_string = " ".join(string_array)
		print(new_string)
	else: 
		new_array = []
		for animal in string_array[:-1]:
			new_animal = animal + ','
			new_array.append(new_animal)
		new_array.append(string_array[-1])
		new_array.insert(-1, "and")
		print(" ".join(new_array))

oxford_comma(animal_string)