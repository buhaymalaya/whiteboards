# you will be given a string and two indexes (a and b). Your task is to reverse the 
# portion of that string between those two indices inclusive.
# solve("codewars",1,5) = "cawedors" -- elements at index 1 to 5 inclusive are "odewa". So we reverse them.
# solve("cODEWArs", 1,5) = "cAWEDOrs" -- to help visualize.
# Input will be lowercase and uppercase letters only.
# The first index a will always be lower that than the string length; the second index 
# b can be greater than the string length. More examples in the test cases. Good luck!
# ex:
# ("FunctionalProgramming", 2,15) => "FuargorPlanoitcnmming"
# ("abcefghijklmnopqrstuvwxyz",0,20) =>"vutsrqponmlkjihgfecbawxyz"

# create empty string ?
# if letter not inside inclusive range, add to string


# slice string

def reverseslice(arr, a, b):
    to_rev = arr[a:b+1] # define the portion from index a to index b to be reversed
    rev_it = to_rev[::-1] # reverse the defined portion
    revised = arr[:a] + rev_it + arr[b+1:] # concatenate part to the left, reversed portion, and part to the right
    return revised

print(reverseslice("FunctionalProgramming", 2,15))
print(reverseslice("abcefghijklmnopqrstuvwxyz",0,20))

# def solve(s, a, b):
#     result = ''
#     for i in range(len(s)):
#         if a <= i <= b:
#             result += s[b - (i - a)]
#         else:
#             result += s[i]
#     return result

# print(solve("FunctionalProgramming", 2, 15))