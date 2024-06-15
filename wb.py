# Find Even numbers
# Create a function that, given a list as a parameter, 
# finds the even numbers inside the list. The function should then return a list.
# Example:
# Input: [2, 7, 10, 11, 12]				
# Output: [2, 10, 12]

# 1 - create a function (list)
# 2 - output = []
# 3 - for n in list
# 4 - output.append(even numbers)
# 5 - return n % 2 == 0

list_nums = [1,2,3,4,5,6]

# def find_even(alist):
#     # output = []
#     for n in alist:
#         return n % 2 == 0
#         # if n % 2 == 0:
#             # output.append(n)
            
# print(find_even(list_nums))

def evens(alist):
    return [n for n in alist if n % 2 == 0]

print(evens(list_nums))

