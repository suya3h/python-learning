# from array import *
# arr = array('i', [])
# n = int(input())
# for i in range(0,n):
#     arr.append(int(input("enter no.")))
    
# largest = max(arr)
# print(largest)


def largest_element(arr):
    max_val = arr[0]

    for i in range(1,len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val    

n = int(input())    
arr = list(map(int, input().split()))

print(largest_element)