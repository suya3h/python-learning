list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))
result = []
for n in list_1:
    if n %2 !=0 :
        result.append(n)
for n in list_2:
    if n%2 ==0 :
        result.append(n)
print(result)        
