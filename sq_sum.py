# Square(n) sum
# Create a function that given a list of 
# integers squares each number passed into it and then 
# sums the results together.
# Example Input: [1, 2, 2]
# Example Output: 9
# Explanation: 1^2 + 2^2 + 2^2 = 9
# Example Input: [3, 4, 5]
# Explanation: 3^2 + 4^2 + 5^2 = 50
# Example Output: 50


def sq_sum(arr):
    # return sum(n**2 for n in arr)
    squared = []
    for n in arr:
        sq = n ** 2
        squared.append(sq)
    
    for n in squared:
        return sum(squared)
    
print(sq_sum([1,2,2]))

    