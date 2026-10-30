nums = [10, 20, 30, 40, 50]

# my_list[start:stop:step] 
# Starting index (inclusive)
# stop	Ending index (exclusive)
# step	How many positions to jump (default = 1)
# nums[:] returns the entire list as a shallow copy.

print(nums[1:3])  # [20, 30]
print(nums[0:3])  # [10, 20, 30]
print(nums[2:])   # [30, 40, 50]
print(nums[:3])   # [10, 20, 30]
print(nums[:])    # [10, 20, 30, 40, 50]

print(nums[-1])    # 50
print(nums[-2])    # 40
print(nums[-3:])   # [30, 40, 50]
print(nums[:-1])   # [10, 20, 30, 40]

# DSA tip: Learn slicing syntax, but don't overuse it in interviews. 
# Slicing creates a new list and generally takes O(k) time and space for k copied elements. 
# For in-place array problems, prefer two pointers when appropriate.