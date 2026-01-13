#Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
number1 = int(input())
number2 = int(input())

if number1 * number2 <1000 :
    print(number1 * number2)
elif number1 * number2>1000:
    print(number1 + number2)