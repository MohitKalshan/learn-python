stack = []

# PUSH - Add elements
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)  # [10, 20, 30]

# POP - Remove top element
stack.pop()

print(stack)  # [10, 20]

# PEEK - Get top element without removing
print(stack[-1])  # 20

# SIZE
print(len(stack))  # 2

# EMPTY CHECK
print(len(stack) == 0)  # False