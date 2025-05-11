#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up
# to n. Print the final sum.
while True:
    n = int (input ("Please pick a positive integer n: "))
    if n > 0:
        break
else:
    print ("That is not a positive integer. Please try again. ")

print (f"You entered: {n}")
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(f"The sum of integers from 1 to {n} is: {sum}")
