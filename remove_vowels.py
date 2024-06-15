# Remove vowels
# Write a function that will remove all vowels from a given string. The function should return a string.
# Examples:                                                                 
# Input: 'Joel'
# Output: 'Jl'                                                     
# Input: 'Shoha'
# Output: 'Shh'


def vowel_removal(input_string):
    vowels = "aeiouAEIOU"
    out_put = []
    for char in input_string:
        if char not in vowels:
            out_put.append(char)
    return ''.join(out_put)

print(vowel_removal('Joel'))


############## More efficient T/S Complexity ##########

def vowel_removal(stringy):
    vowels = "aeiouAEIOU"
    return ''.join([s for s in stringy if s not in vowels ])