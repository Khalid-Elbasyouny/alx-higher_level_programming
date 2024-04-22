#!/usr/bin/python3
"""documentation for the add_integer"""

def add_integer(a, b=98):

	"""function that adds two integers
	argus:
		a: first int
		b: second int with a deffult value as 98
	raises:
		TybeError: if not int's

	returns:
		sum of the int's	
	"""
	if type(a) not in (int, float):
		raise TypeError('a must be an integer')

	if type(b) not in (int, float):
                raise TypeError('b must be an integer')
	return int(a) + int(b)

if __name__ == "__main__":
	import doctest
	doctest.testfile("tests/0-add_integer.txt")
