def is_number_prime(number):
	#Number's 0 and 1 are not prime numbers
	if number == 0:
		return False
		# print("Is 0")
	if number == 1:
		return False
		# print("Is 1")
	
	for x in range(2,number):
		if number % x == 0:
			#return False
			# print("The number is not prime")
			return False
	else:
			#return True
			# print("Its prime")
			return True

result = list(filter(is_number_prime, range(10)))
print(result)


