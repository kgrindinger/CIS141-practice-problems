'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
it. Write a Python program that:
- Reads the file
- Requests 5 inputs from the user: 5 words the user would like to count the frequency of
- Counts how many times each word appears
- Creates a dictionary of the words and their counts
- Print the dictionary to the console
'''
import string

def count_word_frequencies():
    # Read the contents of the file
    with open("song_lyrics.txt", "r") as file:
        lyrics = file.read().lower()

    # Remove punctuation
    lyrics = lyrics.translate(str.maketrans("", "", string.punctuation))

    # Get 5 words from the user
    words_to_count = []
    for i in range(5):
        word = input(f"Enter word {i + 1} to count: ").lower()
        words_to_count.append(word)

    # Split lyrics into words
    word_list = lyrics.split()

    # Count word occurrences
    word_counts = {word: word_list.count(word) for word in words_to_count}

    # Print the result
    print("\nWord Frequencies:")
    print(word_counts)

# Run the program
count_word_frequencies()

