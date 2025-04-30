'''
#Prompt the user for a sentence and a word to try to find in that sentence. Have the program 
print out whether the word was found in the sentence. (i.e. True or False)
'''

sentence = input ("Please write a sentence.")

print ("cloud" in sentence)
'''
Updated solve for this practive problem.
'''

sentence = input ("Please write a sentence.")
word = input ("Please enter a word.")

found = (word in sentence)

print (found)
