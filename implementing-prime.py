def implementing_prime(number):
	if number < 1:
		print("Not a real number.")
	if number == 1 or number == 2:
		print("True")
	else:
		for num in range(2,number):
			if number % num == 0:
				print(f"False, {number} is divisible by {num}.")
				break
		else:
			print(f"{number} Is prime.")

implementing_prime(1)
implementing_prime(2)
implementing_prime(3)
implementing_prime(4)
implementing_prime(5)
implementing_prime(6)
implementing_prime(7)
implementing_prime(8)
implementing_prime(9)
implementing_prime(13)
