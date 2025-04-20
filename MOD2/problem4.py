'''Create a program that prompts the user for their birth year and displays a message that says "You are ___ old".
Use an f-string in your solution to solve this problem.
'''
birth_year = int(input("What year were you born? "))
current_year = int (2025)
age = current_year-birth_year
print(f"You are {age} years old.")
