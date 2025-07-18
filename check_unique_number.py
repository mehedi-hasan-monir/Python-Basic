# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

def all_unique(numbers):
    return len(numbers) == len(set(numbers))

numbers1 = [1,2,2,5,6]
numbers2 = [1,2,3,4,5]

print("Is numbers1 unique? ",all_unique(numbers1))
print("Is numbers2 unique? ",all_unique(numbers2))
