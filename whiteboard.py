# Fizz Buzz 
# Given a random number as an input to a function, 
# return "FIZZ" if the number is even and "BUZZ" if the number is odd	


# Fizz Buzz #2
# Write a function to print all numbers 1 to n, but there are some constraints
# If the number is divisible by 3, print 'Fizz' instead of the number
# If the number is divisible 5, print 'Buzz' instead of the number
# If the number is divisible by both 3 and 5, print 'FizzBuzz' instead of the number
# Otherwise, simply print the number	

def printy(n):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

print(printy(8))

# time complexity 
# linear ie) 0,14 takes 15 steps
# constant takes one step