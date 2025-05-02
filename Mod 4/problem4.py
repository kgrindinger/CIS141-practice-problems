# A theater wants to enforce age restrictions for movie tickets. Ask the user for 
#their age, and tell them whether they can see G (appropriate for under 13), 
#PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.


age = int(input ("What is your current age? "))

if age >= 17:
    print("All ratings allowed")
elif age <=12:
    print ("G rated only")
else:
    print("Only G, PG, and PG-13 movies allowed")
