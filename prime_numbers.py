def is_number_prime(number):
	#Number's 0 and 1 are not prime numbers
	
	
	for x in range(number):
		if number % x == 0:
			#return False
			print("The number is not prime")
		else:
			#return True
			print("Its not prime")


