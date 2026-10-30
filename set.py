# Set

my_set = {1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10}

my_set.add(10)

my_set.remove(1)

print("Set", my_set)


# Important difference: remove() vs discard()

my_set = {1, 2, 3}
my_set.remove(5)  # KeyError
my_set.discard(5)  # No error

# DSA tip: Prefer discard() when you aren't sure whether an element exists.

# Set operations (Very important)
# Python supports mathematical set operations.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union
print(a | b)

# Intersection
print(a & b)

# Difference
print(a - b)

# Symmetric Difference
print(a ^ b)

# 6. Important things to remember
# Empty set:
my_set = set()

# Don't use {} for an empty set. It creates an empty dictionary.


# Set doesn't maintain a guaranteed insertion order. 
# Due to hashing, the order of elements may change when you add or remove elements.
# This is different from lists and tuples, which maintain the order of elements.
# nums = {10, 20, 30}
# print(nums[0])  # TypeError