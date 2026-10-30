# Dictionary in Python (HashMap)

# Python dictionary keys are not restricted to strings. 
# They can be strings, integers, tuples (if hashable), and other hashable objects.
# A Python Dictionary is a collection of key-value pairs, similar to Java's HashMap.

# 1. Java vs Python
# Language	        Data Structure
# C++	            unordered_map
# Java	            HashMap
# JavaScript	    Object / Map
# Python	        dict


# Dictionary

from click import clear


student = {
    "name": "Mohit",
    "age": 25,
    "role": "Developer"
}

print(student) # {'name': 'Mohit', 'age': 25, 'role': 'Developer'}

# Access
print(student["name"])

# Add
student["city"] = "Delhi"

# Update
student["age"] = 30

# Remove
student.pop("city")

# Check key
print("name" in student)

# Length
print(len(student))

print(student)

# 5. Important Dictionary Methods

# Operation	        Python	            Java HashMap
# Insert	       d[key] = value	        put()
# Get	           d.get(key)	            get()
# Remove	       d.pop(key)	            remove()
# Check key	       key in d	                containsKey()
# Get keys	       d.keys()	                keySet()
# Get values	   d.values()	            values()
# Get entries	   d.items()	            entrySet()
# Size	           len(d)	                size()
# Clear     	   d.clear()	            clear()


# Dictionary Looping
# This is particularly important for DSA.

for key in student:
    print(key)

# Loop through values:
for value in student.values():
    print(value)

# Loop through key-value pairs:
for key, value in student.items():
    print(key, value)

# 7. Very Important: Dictionary with Integer Keys

my_dict = {
    1: "Apple",
    2: "Banana",
    3: "Mango"
}

print(my_dict[1])  # Apple

# You can also use tuples as keys:
grid = {}

grid[(0, 0)] = "Start"
grid[(0, 1)] = "Visited"

print(grid[(0, 0)])
# This is useful for graph and matrix DSA problems.

# 8. Dictionary vs Set
# Both use hashing internally.
# Feature	            Set	                Dictionary
# Stores	            Unique elements	    Key-value pairs
# Syntax	            {1, 2, 3}	        {"a": 10}
# Duplicate keys	    Not applicable	    Not allowed
# Duplicate values	    Not applicable	    Allowed
# Access	            Membership	        Key lookup

# Most Important DSA Application: Frequency Counter
# Java vs Python frequency counting
# Map<Integer, Integer> freq = new HashMap<>();

# for (int num : nums) {
#     freq.put(num, freq.getOrDefault(num, 0) + 1);
# }

nums = [1, 2, 2, 3, 3, 3, 4]
# want to count how many times each number appears
freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

print(freq) # Output: {1: 1, 2: 2, 3: 3, 4: 1}

# How does this work?
# For every number:
# - If the key exists, get its current count.
# - If it doesn't exist, use 0.
# - Increase the count by 1.
# This is one of the most frequently used HashMap patterns in coding interviews.

# DSA Problems to Practice
#     Problem	                          Concept
# Two Sum	                        HashMap
# Contains Duplicate	            Set
# Valid Anagram	                    Frequency Counter
# First Unique Character	        HashMap
# Group Anagrams	                HashMap + Sorting
# Subarray Sum Equals K	            Prefix Sum + HashMap
# Longest Consecutive Sequence	    Set


# 1. dict.get() – Get value safely
# In Java: map.get(key);


# In Python: my_dict.get(key)



# The important difference is that Python's get() allows you to provide a default value.
my_dict = { 
             "apple": 10, 
             "banana": 20
        }
print(my_dict.get("apple"))       # 10
print(my_dict.get("mango"))       # None
# 
print(my_dict.get("mango", 0))    # 0 - Not found - return default value 



# How does it work?

# Syntax:
# dictionary.get(key, default_value)

# - If key exists → returns its value.
# - If key doesn't exist → returns default value.
# - If no default is provided → returns None.


# 2. dict.items() – Iterate over key-value pairs

for key, value in my_dict.items():
    print(key, value)

# What does items() return?
# It returns a dictionary view containing key-value pairs as tuples.

# Important: 
# items() returns a view, not a list. 
# It reflects changes made to the dictionary and does not support indexing directly.

# 3. key in dict – Check whether key exists
# Java equivalent: map.containsKey(key);

print("apple" in my_dict)  # True
print("mango" in my_dict)  # False
print(10 in my_dict)            # False
print(10 in my_dict.values())   # True

# You can also use not in.
if "mango" not in my_dict:
    print("Key doesn't exist")

# By default, in checks dictionary keys, not values.