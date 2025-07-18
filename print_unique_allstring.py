# Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'u'. Ensure that each character is used only once.

import itertools

letters = ['a','e','i','o','u']

all_string = itertools.permutations(letters)

print("Possible all string using ['a','e','i','o','u'] are : ",end='\n\n')
for p in all_string:
    print("".join(p),end=" ")