# Add Strings
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# Note:
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# Example:
# Input: num1 = "30", num2 = "10"
# Output: 40
# The output should be given as an integer

def add_strings(num1, num2):
    return int(num1) + int(num2)

print(add_strings('50', '90'))

