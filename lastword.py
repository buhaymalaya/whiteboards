# Length of Last word
# Create a function that given a string as a parameter of upper/lower case letters and empty space characters (" "), return the length of the last word. 
# Meaning, the word that appears far most to the right if we loop through the words.
# Example Input: "Hello World"
# Example Output: 5				
# Example Input: "We're learning about a great full-stack web application called Flask"
# Example Output: 5	

# hello = 'Hello my name is Buhay'

def last_word(stringy):
    separated = stringy.split(" ")
    for x in separated:
        return len(separated[-1])


print(last_word('Hello my name is Buhay'))


def len_last(astring):
    count = 0
    for char in astring[::-1]:
        if char == ' ':
            return count 
        count +=1
    return count

print(len_last('Hello my name is Buhay'))