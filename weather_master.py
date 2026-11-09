"""
File: weather_master.py
Name: Benjamin
-----------------------
This program implements a console-based application that
asks the user to enter weather data and computes summary
statistics based on the inputs.

The program calculates the average, highest, and lowest
temperatures, as well as the number of cold days. The
output format should match the sample run shown in the
Assignment 2 handout.
"""

WEATHER=-100

def main():
	print('stanCode \"Weather Master 4.0!\"')
	data=int(input('Please enter a temperature: '))
	sum = data
	count = 1
	cold_day = 0
	if data == WEATHER:
		print('No data')
	else:
		maximum = data
		minimum = data
		while True:
			data = int(input('Next Temperature: '))
			if data == WEATHER:
				break
			if data > maximum:
				maximum = data
			if data < minimum:
				minimum = data
			if data < 16:
				cold_day = cold_day + 1
			count = count + 1
			sum = sum + data
		print('Highest temperature '+ '= '+ str(maximum))
		print('Lowest temperature ' + '= ' + str(minimum))
		print('Average '+ '= '+ str(sum/count))
		print(str(cold_day)+ ' cold day(s)')







# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
