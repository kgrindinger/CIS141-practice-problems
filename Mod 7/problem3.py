#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
#For example, water is very effective to fight fire.
#Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
#strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
#simple type effectiveness rules. Your solution only needs to work for these three sets of input:

#I just want to write code for the print statements, which is super helpful because I know nothing about Pokeman!

def type_advantage(attacker, defender):
    attacker = attacker.lower()
    defender = defender.lower()

    if attacker == 'fire':
        if defender == 'grass':
            return 'Super Effective'
        elif defender == 'water' or defender == 'fire':
            return 'Not Very Effective'
        else:
            return 'Neutral'
    elif attacker == 'water':
        if defender == 'fire':
            return 'Super Effective'
        elif defender == 'grass' or defender == 'water':
            return 'Not Very Effective'
        else:
            return 'Neutral'
    elif attacker == 'grass':
        if defender == 'water':
            return 'Super Effective'
        elif defender == 'fire' or defender == 'grass':
            return 'Not Very Effective'
        else:
            return 'Neutral'
    elif attacker == 'electric':
        if defender == 'water':
            return 'Super Effective'
        elif defender == 'grass' or defender == 'electric':
            return 'Not Very Effective'
        else:
            return 'Neutral'
    else:
        return 'Neutral'

print(type_advantage("Water", "Fire"))       # Super Effective
print(type_advantage("Fire", "Water"))       # Not Very Effective
print(type_advantage("Electric", "Grass"))   # Not Very Effective

