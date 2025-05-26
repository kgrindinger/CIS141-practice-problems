#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
#For example, water is very effective to fight fire.
#Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
#strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
#simple type effectiveness rules. Your solution only needs to work for these three sets of input:

def type_advantage(attacker, defender):
    effectiveness = {
        'fire': {'grass': 'Super Effective', 'water': 'Not Very Effective', 'fire': 'Not Very Effective'},
        'water': {'fire': 'Super Effective', 'grass': 'Not Very Effective', 'water': 'Not Very Effective'},
        'grass': {'water': 'Super Effective', 'fire': 'Not Very Effective', 'grass': 'Not Very Effective'},
        'electric': {'water': 'Super Effective', 'grass': 'Not Very Effective', 'electric': 'Not Very Effective'},
    }

    attacker = attacker.lower()
    defender = defender.lower()

    if attacker in effectiveness:
        return effectiveness[attacker].get(defender, 'Neutral')
    else:
        return 'Neutral'
        
print(type_advantage("Water", "Fire")) 
print(type_advantage("Fire", "Water")) 
print(type_advantage("Electric", "Grass")) 
