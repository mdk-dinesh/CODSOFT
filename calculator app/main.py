import calculator

def get_number(prompt):
    """Prompts the user for a number and handles invalid input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Simple Calculator CLI")
    print("---------------------")

    while True:
        print("\nOperations:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("Q. Quit")

        choice = input("Enter choice (1/2/3/4/Q): ").upper()

        if choice == 'Q':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '+', '-', '*', '/'):
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            try:
                if choice == '1' or choice == '+':
                    result = calculator.add(num1, num2)
                    op_symbol = "+"
                elif choice == '2' or choice == '-':
                    result = calculator.subtract(num1, num2)
                    op_symbol = "-"
                elif choice == '3' or choice == '*':
                    result = calculator.multiply(num1, num2)
                    op_symbol = "*"
                elif choice == '4' or choice == '/':
                    result = calculator.divide(num1, num2)
                    op_symbol = "/"
                
                print(f"{num1} {op_symbol} {num2} = {result}")

            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid input. Please select a valid operation.")

if __name__ == "__main__":
    main()
