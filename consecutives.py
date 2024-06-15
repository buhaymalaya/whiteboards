# Consecutive Indices
# You are given a list of unique integers (arr), 
# and two integers (a and b). Your task is to find out 
# whether or not a and b appear consecutively in arr, 
# and return a boolean value (True if a and b are consecutive, False otherwise).
# It is guaranteed that a and b are both present in arr.
# Example:
input1 = [1, 6, 9, -3, 4, -78, 0]
a = -3
b = 4
# Output: True
input = [3,1,0,19] 
        #  19, 0
# Output: True

def consec(arr, a, b):
    for i, char in enumerate(arr):
        if arr[i] == a and arr[i+1] == b:
            return True
        elif arr[i] == b and arr[i+1] == a:
            return True
    return False
        
print(consec(input1, 4, -78))
        



#  Carlos solution below

def wb_problem (arr, a, b):
    for x in arr:
        if x == a:
            if b == arr[arr.index(x) + 1]:
                return True
        elif x == b:
            if a == arr[arr.index(x) + 1]:
                return True
    return False

# Tan solution

#  using index() method

def wb(arr, a, b):
    return abs(arr.index(a) - arr.index(b)) == 1

print(wb([88,9,77,4,5], 9, 77))