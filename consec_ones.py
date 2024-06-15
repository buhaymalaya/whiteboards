# Max consecutive Nums:
# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. 
# The maximum number of consecutive 1s is 3.
# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2

# Check which consecutive ones are the maximum length

# def max_ones(arr):
#     count = 0
#     maximum = 0
#     for num in arr:
#         if num == 1:
#             count += 1
#         else:
#             maximum = max(count, maximum)
#             count = 0
#     maximum = max(count, maximum)
#     return count

# print(max_ones([1,0,1,1,0,1]))

def consec(arr):
    arr2 = 0
    count = 0
    for v in arr:
        if v == 1:
            count += 1
        else:
            arr2 = max(count, arr2)
            count = 0
    arr2 = max(count, arr2)
    return arr2


print(consec([1,1,0,1,1,1]))