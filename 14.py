day = input("what day is it today? ")
age = int(input("what is the age of costumer "))

price = 12 if age >= 18 else 8
if day == "wednesday" :
    price = price -2
print (price)    