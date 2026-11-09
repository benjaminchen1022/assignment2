"""
File: quadratic_solver.py
Name: Benjamin
-----------------------
This program implements a console-based solver for a
quadratic equation.

It asks the user to input three values a, b, and c,
and computes the roots of the equation:
ax^2 + bx + c = 0.

The output format should match the sample run shown
in the Assignment 2 handout.
"""

import math


def main():
	data1 = int(input('Enter a: '))
	data2 = int(input('Enter b: '))
	data3 = int(input('Enter c: '))
	root = data2 * data2 - 4 * data1 * data3
	if root > 0:
		y = math.sqrt(root)
		x1 = (-data2 + y) / (data1 * 2)
		x2 = (-data2 - y) / (data1 * 2)
		print('Two roots: '+str(x1)+ ', '+ str(x2))
	elif root == 0:
		y = math.sqrt(root)
		x1 = (-data2 + y) / (data1 * 2)
		print('One root: '+ str(x1))
	else:
		print('No real roots')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
