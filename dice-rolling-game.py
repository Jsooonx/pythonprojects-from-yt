import random

# Session counters
total_rolls = 0
total_dice_rolled = 0

# How many dice per roll?
while True:
    try:
        num_dice = int(input("How many dice do you want to roll each turn? (1-10): "))
        if 1 <= num_dice <= 10:
            break
        else:
            print("Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input, please enter a number.")

print(f"\nYou will roll {num_dice} dice each turn.\n")

while True:
# Ask: roll the dice?
    choice = input("Roll the dice? (y/n/change): ").lower()
    # If user enters y
    if choice == "y":
        results = [random.randint(1, 6) for _ in range(num_dice)]
        
        total_rolls += 1
        total_dice_rolled += num_dice
        
        print(f"You rolled: {results}")
        print(f"Total: {sum(results)}")
        print(f"This session: {total_rolls} roll(s) | {total_dice_rolled} dice rolled total.\n")
        
    elif choice == "change":
        while True:
            try:
                num_dice = int(input("Change to how many dice? (1-10): "))
                if 1 <= num_dice <= 10:
                    print(f"Got it, now rolling {num_dice} dice!\n")
                    break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input, please enter a number.")
                
    # If user enters n
    elif choice == "n":
        #   Print thank you message
        print("\nThanks for playing!")
        print("Session summary:")
        print(f"    - Total rolls: {total_rolls}")
        print(f"    - Total dice rolled: {total_dice_rolled}")
        break
    else:
        #   Print invalid choice
        print("Invalid choice! Type 'y', 'n', or 'change'.")