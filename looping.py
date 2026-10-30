

nums = [10, 20, 30, 40, 50]

# 1. Normal for loop (Using Index)

for i in range(len(nums)):
    print(nums[i])

# 2. Direct iteration (Enhanced for loop)
# Python's most common way to iterate over a list.
# When to use: When you only need the values, not their indexes.

for num in nums:
    print(num)


# 3. Using enumerate() (Index + Value)
# Very useful in DSA.

for index, value in enumerate(nums):
    print(index, value)

# 4. Using range() with Step
# You can control how many indexes you skip.

for i in range(0, len(nums), 2):
    print(nums[i])

# 5. Reverse Looping
# Using range()

for i in range(len(nums) - 1, -1, -1):
    print(nums[i])

# --------------- while loop ---------------

# 6. While Loop
# Useful when you need manual control over the index.

i = 0

while i < len(nums):
    print(nums[i])
    i += 1

# 7. Nested Looping
# Important for 2D arrays and matrix problems.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

# 8. Looping with break and continue
# Break: Terminates the loop.

for num in nums:
    if num == 30:
        break
    print(num)

# Continue: Skips the current iteration.

for num in nums:
    if num == 30:
        continue
    print(num)