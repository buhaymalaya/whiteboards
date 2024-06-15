# Find Middle Number
# Given a number (n) and an array of numbers (num_list) as input to a function, 
# return True if the number is greater than the middle number of the array. 
# Return False if the number is less than the middle number of the array.
# Example Input: n = 6, array = [3,5,8, 10]			
# Example Output: True
# Example Input: n = 105, array = [10,30,44,22,100]
# Example Output: True

def find_middle(n, numlist):
    return n> numlist[(len(numlist)-1)//2] 

    # middle = (len(numlist) - 1) // 2
    # if n > numlist[middle]:
    #     return True
    # else:
    #     return False
    
print(find_middle(2, [3,5,8,10]))