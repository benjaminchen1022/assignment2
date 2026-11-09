"""
File: extension1_factorial.py
Name: 
-------------------
This program repeatedly asks the user to enter a number
and calculates the factorial of that number.

The result is printed to the console.
The program will stop running when the user enters the EXIT value.
"""

EXIT = -100

def main():
	print('Welcome to stanCode factorial master!')
	data = int(input('Give me a number, and I will list the answer of factorial: '))
	if data == EXIT:
		print('-----See ya!-----')
	else:
		while True:
			count = 1
			if data == EXIT:
				print('-----See ya!-----')
				break
			else:
				for i in range(1, data+1):
					n1 = count * i
					count = n1
				print(str(n1))
				data = int(input('Give me a number, and I will list the answer of factorial:'))







				# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()