# Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
# Example 4:
# Input: nums = [1,3,5,6], target = 0
# Output: 0
# Example 5:
# Input: nums = [1], target = 0
# Output: 0

# def search_pos(arr, target):
#     for i in range(len(arr)-1):
#         if target in arr:
#             return arr[i]
        
# print(search_pos([1,3,5,6], 5))

# def search_pos(arr, target):
#     new = []
#     for i, v in enumerate(arr):
#         left = arr[i]
#         right = arr[i+1]
#         if target == v:
#             return i
#         elif target not in arr:
#             left < target < right
#             new.append(left, target, right)
#             return new
            

def search_pos(arr, target):
    left = 0 
    right= len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
        
print(search_pos([1,3,5,6], 4))

# if target not found in arr, compare target to values in the arr
# element to the left must be less than value while element to the right must be greater than value
# once position is found, decipher its index

