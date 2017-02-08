def is_number_prime(number):
	#Number's 0 and 1 are not prime numbers thus you eliminate them
	if not isinstance(number, int):
		return "input parameter is not an int"
	if number >= 10*10:
		return "number is too large"
	if number < 0:
		return False
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


