def ask_continue():
    while True:   
        should_continue = input("Continue? (y/n): ").lower()
        if should_continue == 'y':
            break
        elif should_continue == 'n':
            print("Thanks for using the calculator!")
            exit()
        else:
            print("Invalid choice! Choose 'y' or 'n'.")
        
while True:
    print("Welcome to the Python Calculator!")
    print("=" * 33)
    
    while True:
        try:
            num1 = float(input("Enter the 1st number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    while True:
        try:
            num2 = float(input("Enter the 2nd number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    while True:
        operator = input("Enter an operator (+ - * /): ")
        
        if operator == '+':
            result = num1 + num2
            print(round(result, 3))
        elif operator == '-':
            result = num1 - num2
            print(round(result, 3))
        elif operator == '*':
            result = num1 * num2
            print(round(result, 3))
        elif operator == '/':
            result = num1 / num2
            print(round(result, 3))
        else:
            print(f"{operator} is an invalid operator!")
            continue
        break
        
    ask_continue()