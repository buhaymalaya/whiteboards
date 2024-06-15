# Lucky Numbers
# Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
# Example 1:
# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:
# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

# a lucky integer is n = count(n)

def lucky_integer(arr):
    new = []
    
    for n in arr:
        if n == arr.count(n):
            new.append(n)

    if not new:
        return -1
        
    return max(new)
        
print(lucky_integer([1,2,2,3,3,3,4,4,4]))
    

# def lucky_num(arr):
#     nums = {}
#     count = 0
#     for k, v in arr.items():
#         if nums[k] == count:
#             return max(count)
        
# print(lucky_num([1,2,2,3,3,3,4,4,4]))


### Tan's Solution with dictionary

def lucky(arr):
    freq = {}
    for i in range(0,len(arr)):
        if arr[i] not in freq:
            freq[arr[i]] = 1
        else:
            freq[arr[i]] += 1
    print(freq)
    lst = []
    if len(lst) > 0:
        for k,v in freq.items():
            if k == v:
                lst.append(k)
        return max(lst)
    return -1