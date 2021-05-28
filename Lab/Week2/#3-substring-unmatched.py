####### Problem 3 #############
# Assuming there are two words, wrd1 & wrd2, we say wrd1 is a sub-sequence of wrd2 if all the letters in wrd1 appear in wrd2 in the same order (but not necessarily contiguous). That is, you can add letters to any position in wrd1 to get wrd2. For instance, "song" is a substring of "absorbing" and "coast" is a substring of "contrast".
# Create a function add_char in recursion, taking in wrd1 & wrd2, where wrd1 is a substring of wrd2, which means that wrd1 is shorter than wrd2, and return value is a string containing the characters you need to add to wrd1 to get wrd2. 
# In the example above, you need to add the characters "abrbi" to "song" to get "absorbing", and you need to add "ntr" to "coast" to get "contrast".
# The letters in the string you return should be in the order you have to add them from left to right. If there are multiple characters in the wrd2 that could correspond to characters in wrd1, use the leftmost one. For example, add_char("toy", "tacophony") should return "acphon", not "caphon" because the first "t" in "toy" corresponds to the first "t" in "tacophony".

# def add_char(wrd1, wrd1):

#     """
#     Return a string containing the characters you need to add to wrd1 to get   wrd2.

#     add_char("eel", "heel")
#     'h'
#     add_char ("we", "wean")
#     'an'
#     add_char("rot", "rotation")
#     'ation'
#     add_char("a", "appropriate")		
#     'ppropriate'
#     add_char ("vax", "anit-vaxxer")
#     'anti-xer'
#     add_char("facy", "efficacy")
#     'efic'
#     add_char("toy", "tacophony")
#     'acphon'
    
#     """
#     """ Write your program here"""

def add_char(wrd1, wrd2):
    if(not(len(wrd1))): #if no more substring left to check, return all remaining 
        return wrd2
    elif (wrd1 in wrd2): #if entire word matches, remove matching string from second word
        removeWord = wrd1
        wrd1 = wrd1.replace(removeWord, '', 1)
        wrd2 = wrd2.replace(removeWord, '', 1)
        return add_char(wrd1, wrd2)
    else: #check letter by letter and remove matching letter from both word
        removeWord = wrd1[0]
        wrd1 = wrd1.replace(removeWord, '', 1)
        wrd2 = wrd2.replace(removeWord, '', 1)
        return add_char(wrd1, wrd2)


print(add_char("eel", "heel"))
print(add_char("we", "wean"))
print(add_char("rot", "rotation"))
print(add_char("a", "appropriate"))		
print(add_char("vax", "anti-vaxxer"))
print(add_char("facy", "efficacy"))
print(add_char("toy", "tacophony"))
print(add_char("coast", "contrast"))

