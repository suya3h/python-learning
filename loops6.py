given = input()

for char in given:
    if char.count(char) == 1:
        print(char)
        break