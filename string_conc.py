# Given 2 string parameters, show a concatenation of:
# the reverse of the 2nd string with inverted case; e.g Fish -> HSIf
# a separator in between both strings: @@@
# the 1st string reversed with inverted case and then mirrored; 
# e.g Water -> RETAwwATER 
# Test cases:
# ('FizZ', 'buZZ') -> 'zzUB@@@zZIffIZz'
# ('String Reversing', 'Changing Case') -> 
# 'ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING'

a = 'FizZ'
b = 'buZZ'
c = 'String Reversing'
d = 'Changing Case'

def concky(str1, str2):
    return str2.swapcase()[::-1] + '@@@' + str1.swapcase()[::-1] + str1.swapcase()

print(concky(a, b))
print(concky(c, d))