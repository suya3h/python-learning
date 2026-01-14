word = input()
n = int(input())
def remove_chars(word, n):
     remove_chars = word[n:]
     return(remove_chars)

print(remove_chars(word,n))