#5. Write a function called level_up(experience) that takes a player's experience
#points and returns their new level based on these rules:
#* 0-99 XP → Level 1
#* 100-199 XP → Level 2
#* 200+ XP → Level 3

#OK, so I want to ask what the curent score or XP is and then tell them which level they are at. So, input first then function.

def level_up(experience):
    if experience < 100:
        return 1
    elif experience < 200:
        return 2
    else:
        return 3

def main():
    score_input = input("What is your current XP? ")
    
    try:
        experience = int(score_input)
        level = level_up(experience)
        print(f"You are now at Level {level}!")
    except ValueError:
        print("Please enter a valid number.")

main()
 
