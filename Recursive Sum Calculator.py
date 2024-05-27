# Recursive Sum Calculator
# Created by: Ibrahim Yisau
# Date: May 27, 2024
#
# This program calculates the sum of numbers from 0 to n using a recursive function.
# ==================================================================================
# Define a recursive function to calculate the sum of numbers from 0 to n
def recursive_sum(n):
	"""
	Calculate the sum of numbers from 0 to n using recursion.

	Args:
		n (int): The upper limit of the numbers to be summed.

	Returns:
		int: The sum of numbers from 0 to n.
	"""
	if n == 0:
		# Base case: return 0 when n is 0
		return 0
	else:
		# Recursive case: call recursive_sum with n-1 and add n
		return recursive_sum(n-1) + n

# Test the function
print(recursive_sum(15))
