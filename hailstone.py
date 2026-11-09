"""
File: hailstone.py
Name: Benjamin
-----------------------
This program implements a console-based simulation of the
Hailstone sequence, as defined by Douglas Hofstadter.

Starting from a user-provided number, the program repeatedly
applies the Hailstone rules and prints each step. The output
format should match the sample run shown in the Assignment 2 handout.
"""


def main():
    print('This program computes hailstone sequences')
    n = int(input('Please enter a number: '))
    while n != 1:
        if n % 2 == 1:
            new_n = n * 3 + 1
            print(str(n)+ ' is odd, so I make 3n+1: '+ str(new_n))
            n = new_n
        else:
            new_n = n//2
            print(str(n)+ ' is even, so I take half: '+ str(new_n))
            n = new_n


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
