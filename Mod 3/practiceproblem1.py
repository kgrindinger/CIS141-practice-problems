# Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.
random_word = input("Please pick a random word ")

num_times = input ("How many times shall I repeat your word?")

answer = (random_word) * (int(num_times))

print (answer)
