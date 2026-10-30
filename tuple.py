# A Tuple is an ordered collection of elements,
# similar to a List, but it is immutable (cannot be modified after creation).

# 1. What does immutable mean?
# Immutable means you cannot change the contents of an object after creating it.

# 2. Why did Python introduce immutable tuples?
# There are four important reasons.

# Reason 1: Data safety
# Suppose you store coordinates of a location: 
position = (10, 20)
# You want these coordinates to remain unchanged accidentally.
# With a tuple, reassignment of an element is prevented.


# Reason 2: Hashability (Very important for DSA)
# Tuples containing hashable elements can be used as keys in dictionaries and elements in sets.
visited = set()
visited.add((1, 2))
visited.add((3, 4))
print((1, 2) in visited)  # True

# Why?
# Hash-based collections rely on an object's hash remaining stable while it is stored in the collection.
# A mutable list cannot be used as a set element:
# visited = set()
# visited.add([1, 2])  # TypeError: unhashable type: 'list'

# Reason 3: Predictability
# Imagine you pass a tuple to another function.
def display(position):
    print(position)

coordinates = (10, 20)

display(coordinates)
# The function cannot accidentally replace an individual tuple element.
# This makes tuples useful for passing fixed groups of values.


# Reason 4: Performance and memory
# Tuples are generally more memory-efficient than lists when storing a fixed collection of elements.
# They also have slightly less overhead because they don't need to support resizing.

# Important Interview Concept: Tuple Immutability is Shallow
# This is a tricky Python concept.
data = ([10, 20], 30)

data[0] = [100, 200]  # Error

# recommendation for DSA: Pay special attention to tuple hashing. 
# It is particularly useful in BFS, grid traversal, graph problems and visited sets.

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

# 4. Important Interview Concept: Tuple Immutability is Shallow
# This is a tricky Python concept.

# Consider:
data = ([10, 20], 30)
data[0] = [100, 200]  # Error

# But:
data = ([10, 20], 30)
data[0].append(30)
print(data)

# Output: ([10, 20, 30], 30)

# Why?
# - The tuple structure cannot change.
# - But the list stored inside the tuple is mutable.
# So, tuple immutability does not automatically make nested objects immutable.