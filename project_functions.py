def naive_evaluation(coeff, x):
	
	degree = len(coeff) - 1 # Calculate the degree of the polynomial (highest power)
	result = 0 # Initialize the result accumulator
	
	# Loop through each coefficient and corresponding power of x
	for i in range(degree + 1):
		result += coeff[i] * (x ** i) # Multiply the coefficient by x raised to the current power and add to result
	
	return result # Return the final evaluated value


def horner_rule(coef, x):
	degree = len(coef) - 1 # Calculate the degree of the polynomial (highest power)
	result = 0 # Initialize the result accumulator
	
	# Loop through the coefficients in reverse order (from highest degree to lowest)
	for i in range(degree, -1, -1):
		result = result * x + coef[i] # Multiply the current result by x and add the current coefficient
	
	return result # Return the final evaluated value