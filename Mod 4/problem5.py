# A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, 
# shipping is free. Ask the user for the order total and print the total cost, 
# including shipping.

import math
order = float(input ("What is your order total? $"))

if order < 50:
    shipping = 5.00
    
else:
    shipping = 0.00

total_cost = order + shipping

print (f"order: ${total_cost:.2f}")
print (f"shipping: ${shipping:.2f}")
print (f"Total Cost: ${total_cost:.2f}")
