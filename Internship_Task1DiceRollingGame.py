import random

print("Hi Welcome to the Dice Rolling Game..".title())
def diceroll(): 
    while(True): 
        dice1 = random.randrange(1,6)
        dice2 = random.randrange(1,6)
        print(f"Dice#1: {dice1} \nDice#2: {dice2}")
        print(f"The result is {dice1 + dice2}")  
        usr = input("Do you want to continue (y/n): ").lower()
        if usr != "y":
            print("Thank You for Playing The Game")
            break
if __name__ == "__main__":
    diceroll()
