nums = [10, 20, 30, 40, 50]

# 1. Slicing — Extract elements

test = nums[:]
print(test)

# 2. Splicing — Replace elements using slice assignment

nums[1:4] = [200, 300]
print(nums)



# Replace one element

nums[1:2] = [100]
print(nums) # [10, 100, 30, 40]

# Insert elements

nums[1:1] = [15, 17]
print(nums) # [10, 15, 17, 20, 30]

# Delete elements

nums[1:4] = []
print(nums) # [10, 50]



# 4. Java vs Python comparison

# Operation     	        Java	                                Python

# Extract subarray	    Arrays.copyOfRange()	                nums[1:4]
# Replace elements	    Manual loop / ArrayList.set()	        nums[1:4] = [...]
# Insert elements	    list.addAll()	                        nums[1:1] = [...]
# Delete range	        subList().clear()	                    del nums[1:4]
# Copy list	            new ArrayList<>(list)	                nums[:]

# 5. Important DSA distinction
# Python calls this slice assignment, rather than a separate splice() method like JavaScript's Array.splice().

# Also remember:
# - nums[1:4] → Returns a new list.
# - nums[1:4] = [...] → Modifies the original list.
# - del nums[1:4] → Deletes elements from the original list.