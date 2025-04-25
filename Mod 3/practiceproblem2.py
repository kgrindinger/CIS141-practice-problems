# Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print 
"Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."# Write your code here :-)

user_name = input ("What is your name?")
print ("Hello,",user_name)

age1 = int(input ("How old are you?"))
age2 = age1 + 1

print (f"Hello, {user_name}. You are {age1} years old. Next year, you will be {age2} years old.")
