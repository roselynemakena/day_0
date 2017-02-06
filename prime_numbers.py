def is_number_prime(number):
	#Number's 0 and 1 are not prime numbers thus you eliminate them
	if number == 0:
		return False
	if number == 1:
		return False
	
	for x in range(2,number):
		if number % x == 0:
			return False
	else:
			return True

result = list(filter(is_number_prime, range(10)))
print(result)


