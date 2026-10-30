# A Tuple is an ordered collection of elements,
# similar to a List, but it is immutable (cannot be modified after creation).

# Coming from Java, you can think of it as a lightweight, fixed collection of values,
# although it is not exactly equivalent to a Java array.

# uses parentheses () to create tuples.
# You can also create a tuple without parentheses:

my_tuple = (10, 20, 30, 40, 50)
my_tuple = 10, 20, 30

print(my_tuple)
print(type(my_tuple))

# my_tuple[1] = 100  # TypeError

nums = (10, 20, 30, 20, 40)

# Length
print(len(nums))  # 5

# Count occurrences
print(nums.count(20))  # 2

# Find index
print(nums.index(30))  # 2

# Membership
print(20 in nums)  # True

# Slicing
print(nums[1:4])  # (20, 30, 20)


# 6. Tuple with a Single Element
# This is a common Python interview question.
# Remember: A comma is required to create a single-element tuple.

a = (10)
b = (10,)

print(type(a))  # <class 'int'>
print(type(b))  # <class 'tuple'>

# Tuple Unpacking
# Very useful in DSA.

point = (10, 20)

x, y = point

print(x)  # 10
print(y)  # 20

# swap variables without a temporary variable:

a = 10
b = 20

a, b = b, a

print(a, b)  # 20 10


# Where are Tuples Used in DSA?
# One important use is storing coordinates and graph edges.

# Example: Grid coordinates
position = (2, 3)

row, col = position

print(row)
print(col)

# Example: BFS in a grid
from collections import deque

queue = deque()
queue.append((0, 0))

row, col = queue.popleft()
print(row, col)

# Example: Dictionary keys
# Tuples containing hashable elements can be used as dictionary keys.

visited = set()

visited.add((1, 2))
visited.add((2, 3))

print((1, 2) in visited)  # True

# These four form the foundation of Python collections
# list → Dynamic array.
# tuple → Immutable ordered collection.
# set → Unique elements using hashing.
# dict → Key-value pairs using hashing.