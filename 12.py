n = int(input())
digit = 0
rev = 0
while n !=0:
    digit = n % 10
    n = n // 10
    print(digit , end = " ")
    rev = rev *10 +digit
    