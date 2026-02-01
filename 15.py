marks = int(input())

if marks >101 :
    print("error, wrong marks")
    exit()
if marks < 100 and marks > 89 :
    print("Grade A")
elif marks <= 89 and marks > 79:
    print("Grade B")    
elif marks <= 79 and marks > 69:
    print("Grade C")
elif marks <= 69 and marks > 59:
    print("Grade D")
else : print("Grade F")    