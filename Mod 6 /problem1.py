#Create a list of integers (you get to pick!). Write code to iterate through the list and 
#calculate the sum of all even numbers. Print the resulting sum.

# Using jersey numbers of Arsenal mens team:

numbers = [22, 2, 3, 4, 6, 12, 15, 18, 17, 33, 5, 8, 20, 41, 23, 7, 29, 9, 11, 19]
even_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num
print (f"The sum of all even numbers is: {even_sum}")
