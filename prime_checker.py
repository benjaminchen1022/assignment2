"""
File: prime_checker.py
Name: Benjamin
-----------------------
This program asks the user to enter a number and checks whether
the number is a prime number.

When the program starts, it first prints a welcome message to
the console. It then repeatedly prompts the user to enter an
integer greater than 1 and determines whether the number is prime.

The program will stop running when the user enters the EXIT value.
"""
import math

EXIT = -100

def main():
	print('Welcome to the prime checker')
	data = int(input('n: '))
	if data == EXIT:
		print('Have a good one!')
	while True:
		count = 0
	# 把count當成是輸入data的因數數量
		if data == EXIT:
			print('Have a good one!')
			break
		for i in range(1, data+1):
			if data % i == 0:
				count = count + 1
		if count == 2:
			print(str(data)+ ' is a prime number.')
		else:
			print(str(data)+ ' is not a prime number.')
		data = int(input('n: '))




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
