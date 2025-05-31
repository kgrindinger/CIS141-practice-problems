'''
#2. Write a Python program that allows users to log their hiking trips. The program
should:
- Use a while loop to repeatedly ask for a hike name and distance in miles
- Save each entry to hiking_log.txt (each hike on a new line)
- When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''

def log_hiking_trip():
    filename = "hiking_log.txt"

    print("Welcome to the Hiking Log!")
    print("Enter your hikes. Type '0' as the hike name to quit.\n")

    while True:
        hike_name = input("Enter hike name (or '0' to quit): ")
        if hike_name == "0":
            break

        try:
            distance = float(input("Enter distance in miles: "))
        except ValueError:
            print("Please enter a valid number for distance.\n")
            continue

        with open(filename, "a") as file:
            file.write(f"{hike_name} - {distance} miles\n")
        print("Hike logged!\n")

    print("\nYour Hiking Log:")
    try:
        with open(filename, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No hiking log found.")

log_hiking_trip()

