# Find Smallest Number - (Without min)
# Create a function that given a list of numbers finds the lowest number in the list and returns it.
# Example Input: [50,30,4,2,11,0]
# Example Output: 0
# Example Input 2: [40,3,4,2]
# Example Output 2: 2

def smallest_number(a_list):
    minimum_number = a_list[0] # we are setting minimum value to first index then we iterate later
    for n in a_list: # now we iterate through the list given
        if n < minimum_number: # we check if n (each element) in list is less than the default above
            minimum_number = n # if it is less than, we reset the min number to n
    return minimum_number 

print(smallest_number([50,30,4,2,11,0]))
