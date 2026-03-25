import random

# Loop
while True:
# Ask: roll the dice?
    choice = input("Roll the dice? (y/n): ").lower()
    # If user enters y
    if choice == "y":
        #   Generate two random numbers
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        #   Print them
        print(f'({dice1}, {dice2})')
    # If user enters n
    elif choice == "n":
        #   Print thank you message
        print("Thanks for playing!")
        #   Terminate
        break
    # Else
    else:
        #   Print invalid choice
        print("Invalid choice!")