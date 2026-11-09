"""
File: extension4_narcissistic_checker.py
Name: Benjamin
------------------------
This program repeatedly asks the user to enter a number and checks
whether the number is a narcissistic number.

A positive integer is called a narcissistic number if it is equal to
the sum of its own digits, where each digit is raised to the power of
the total number of digits.

For example, 153 is a narcissistic number because
1^3 + 5^3 + 3^3 = 153. By this definition, all single-digit numbers
are also considered narcissistic.

The program will stop running when the user enters the EXIT value.
"""

EXIT = -100

def main():
    print('Welcome to the narcissistic number checker!')
    data = int(input('n: '))
    if data == EXIT:
        print('Have a good one!')
    else:
        while True:
            if data == EXIT:
                print('Have a good one!')
                break
            else:
                count = 0
                n = data
                #確認有幾位數
                while n > 0:
                    n = n // 10
                    count += 1
                #接下來每個數字加總
                n = data
                total = 0
                while n > 0:
                    n2 = n % 10
                    total = total + n2 ** count
                    n = n//10
                if total == data:
                    print(str(data)  + ' is a narcissistic number')
                else:
                    print(str(data) + ' is not a narcissistic number')
                data = int(input('n: '))

if __name__ == '__main__':
    main()
