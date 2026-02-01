n = list(map(int,input(). split()))
sum_even = 0
for i in n:
    if i % 2 ==0 :
        sum_even = sum_even + i
print(sum_even)        