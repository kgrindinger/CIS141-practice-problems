'''
#Prompt the user for: a word, a first index, and a last index. 
Slice the word at the indexes provided by the user and print to the screen.
'''

str = (input ("Please type a word."))

index1 = (input ("Please pick a first index "))
index2 = (input ("Please pick a last index "))
print (str [0:5])
'''
Updated solve for practice problem 4
'''

word = (input ("Please type a word."))

begin_index = (int(input ("Enter a first index")))

end_index = (int(input ("Enter a last index")))

sliced_word = word [begin_index:end_index]

print (sliced_word)
