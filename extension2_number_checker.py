"""
File: extension2_number_checker.py
Name:
------------------------
This program repeatedly asks the user to enter a number and checks
whether it is a perfect, deficient, or abundant number.

A perfect number is equal to the sum of all its factors excluding
itself. An abundant number has a factor sum greater than the number
itself, while a deficient number has a factor sum smaller than the number.

The program will stop running when the user enters the EXIT value.
"""

EXIT = -100

def main():
    print('Welcome to the number checker!')
    data = int(input('n: '))
    if data == EXIT:
        print('Have a good one!')
    else:
        while True:
            count = 0
            if data == EXIT:
                print('Have a good one!')
                break
            else:
                for i in range(1, data+1):
                    if data % i == 0:
                        n = count + i
                        count = n
                if data == count - data:
                    print(str(data) + ' is a perfect number')
                elif data < count - data:
                    print(str(data) + ' is an abundant number')
                else:
                    print(str(data) + ' is a deficient number')
            data = int(input('n: '))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
