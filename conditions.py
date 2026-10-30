#----- Java vs Python Cheat Sheet --------

#    Java	                   Python

# if (condition)	        if condition:
# else if	                elif
# else	                    else:
# &&	                    and
# \|\|	                    or
# !condition	            not condition
# true	                    True
# false	                    False
# null	                    None
# condition ? a : b	        a if condition else b

# ----------------------------------------------------

# Python uses indentation instead of curly braces {}.

# There are four important concepts:
# 1. if
# 2. if-else
# 3. if-elif-else
# 4. Nested conditions

from platform import node


marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# 4. Nested If
# An if statement inside another if.

num = 15

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Negative or Zero")


# 7. Membership Operators
# Very useful in Python DSA.
# Python provides in and not in.

nums = [10, 20, 30, 40]

if 20 in nums:
    print("Found")

if 50 not in nums:
    print("Not Found")

# 8. Ternary Operator
# String result = (age >= 18) ? "Adult" : "Minor";

age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)


# 9. Identity Operators: is and is not
# These check whether two variables refer to the same object, not merely whether their values are equal.

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False
# == checks value equality.
# is checks object identity.

# Use is None when checking for None:
if node is None:
    print("No node")
# This is especially common in LinkedList and Tree DSA problems.