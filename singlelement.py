# Find Single Number
# Given a non-empty array of integers nums, 
# every element appears twice except for one. Find that single one.
# Example 1:
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
# Input: nums = [4,1,2,1,2]                                                    
# Output: 4
# Example 3:
# Input: nums = [1]
# Output: 1

def single_num(arr):
    set_arr = set(arr)
    for num in set_arr:
        if arr.count(num) == 1:
            return num

#  dictionary way

  

print(single_num([4,1,2,1,4, 8, 2,10,10,20,20,90,999,8]))