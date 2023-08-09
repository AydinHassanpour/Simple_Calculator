import math

def calculator():
    while True:
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Quit")

        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice == '6':
            print("Calculator closed.")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = num1 + num2
                operator = '+'
            elif choice == '2':
                result = num1 - num2
                operator = '-'
            elif choice == '3':
                result = num1 * num2
                operator = '*'
            elif choice == '4':
                if num2 == 0:
                    print("Cannot divide by zero!")
                    continue
                result = num1 / num2
                operator = '/'

            # Display the calculation result
            print(f"{num1} {operator} {num2} = {result}")

        elif choice == '5':
            num = float(input("Enter a number: "))
            if num < 0:
                print("Cannot calculate square root of a negative number!")
            else:
                square_root = math.sqrt(num)
                # Display the square root result
                print(f"Square root of {num} = {square_root}")

        else:
            print("Invalid choice!")

# Call the calculator function to start the program
calculator()

