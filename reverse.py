# Reverse a String in a list
# Write a function that reverses a string. The input string is given as 
# an array of characters char[].
# Do not allocate extra space for another array, 
# you must do this by modifying the input array in-place with O(1) 
# extra memory.
# You may assume all the characters consist of printable ascii characters.

# Example 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# def reverse_string(a_list):
#     return a_list[::-1]

# print(reverse_string(["h","e","l","l","o"]))
# print(reverse_string(["H","a","n","n","a","h"]))

def reverse_string(a_list):
    start = 0
    end = len(a_list) - 1

    while start > end:
        a_list[start] = a_list[end]
        start += 1
        end -= 1

     
print(reverse_string(["h","e","l","l","o"]))
