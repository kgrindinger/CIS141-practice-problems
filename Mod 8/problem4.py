'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated
by commas. Write a program that reads the poll.txt file
Count how many votes "yea" or "nay" received and print the results.
'''

def count_votes():
    # Assumes poll.txt exists and is properly formatted
    with open("poll.txt", "r") as file:
        votes = file.read().strip().lower().split(",")

    # Count the votes
    yea_count = votes.count("yea")
    nay_count = votes.count("nay")

    # Print the results
    print("Vote Results:")
    print(f"Yea: {yea_count}")
    print(f"Nay: {nay_count}")

# Run the program
count_votes()


