#1. Write a function called count_vowels(input) that takes a string
# and returns the number of vowels (a, e, i, o, u) in it.

#I will use some book titles that I can see from my current position as the testers
#input strings
#output boolean
# I want to see the number of vowels per word, per title

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
    
print(count_vowels("Snowblind"))
print(count_vowels("Gaslight"))
print(count_vowels("The Craftsman"))
print(count_vowels("Neuromancer"))
print(count_vowels("The Purity of Venegence"))
print(count_vowels("Bad Actors"))

    
