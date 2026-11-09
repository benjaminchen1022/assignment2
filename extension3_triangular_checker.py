"""
File: extension3_triangular_checker.py
Name: Benjamin
--------------------------
This program repeatedly asks the user to enter a number and checks
whether the number is a triangular number.

A triangular number (Tn) can be represented as a triangular arrangement
of points, where the first row contains one element and each subsequent
row contains one more element than the previous one.

The nth triangular number can be calculated using the formula:
Tn = n(n + 1) / 2.

The program will stop running when the user enters the EXIT value.
"""

EXIT = -100

def main():
    print('Welcome to the triangular number checker!')
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
                for i in range(1, data + 1):
                    if i * (i + 1)//2 == data:
                        count += 1
                if count == 1:
                    print(str(data) + ' is a triangular number')
                else:
                    print(str(data) + ' is not a triangular number')
            data = int(input('n: '))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
