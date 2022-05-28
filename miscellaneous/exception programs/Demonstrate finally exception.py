# Python program to demonstrate finally


try:  # No exception Exception raised in try block
	k = 5//0 
	print(k)

except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')
