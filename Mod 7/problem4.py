#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
#State Ferry fare based on age and whether the person has a vehicle. Assume the following rates:
#* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
#* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
#* Children (0-18): Free.

# I am going to challenge myself here as I want to include an input statement that asks how many people are riding and then give a total amount for the crossing. 
#Start with input string, then wrap in function. 

def ferry_fare(age,vehicle):
    if age <= 18:
        return 0.0  
    elif 19 <= age <= 64:
        return 20.0 if vehicle else 10.0  
    elif age >= 65:
        return 15.0 if vehicle else 5.0  
    else:
        return None  
        
def main():
    total_fare = 0.0
    num_people = int(input("How many people are riding the ferry? "))

    for i in range(num_people):
        print(f"\n--- Person {i + 1} ---")
        age = int(input("Enter age: "))
        vehicle_input = input("Are they bringing a vehicle? (yes/no): ").strip().lower()
        vehicle = vehicle_input == "yes"
        
        fare = ferry_fare(age, vehicle)
        print(f"Fare for this person: ${fare:.2f}")
        total_fare += fare

    print(f"\nTotal fare for all passengers: ${total_fare:.2f}")
main()
