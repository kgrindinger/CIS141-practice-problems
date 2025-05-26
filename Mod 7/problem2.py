# Problem 2: Write a function called is_palindrome(s) that checks whether a string is a palindrome
# (reads the same forward and backward, ignoring case). The function should
# returns either True or False.

#test: make good sampling of palindrome and a few that are not to ensure proper answering
#Input: string (s)
#Output: boolean
#Function body: lower case original string, flip it and compare s and flipped_s

def is_palindrome(s):
    lower_s = s.lower()
    flipped_s = lower_s[::-1]
    return lower_s == flipped_s
    
print (is_palindrome("level"))
print (is_palindrome("radar"))
print (is_palindrome("ritual"))
print (is_palindrome("madam"))
print (is_palindrome("kayak"))
print (is_palindrome("skin"))
