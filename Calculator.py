# Simple Calculator

def calculator():
    print("Welcome to Simple Calculator!")
    
    # Input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Choose operation
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Modulus(%)")
    print("5. Division (/)")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    # Perform calculation
    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    elif choice == '4':
        result = num1 % num2
        operation = "%"
    elif choice == '5':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        operation = '/'
    else:
        print("Invalid choice!")
        return

    # Display result
    print(f"\nResult: {num1} {operation} {num2} = {result}")

# Run calculator
calculator()