def calculator():
    while True:  # Loop to allow restarting
        try:
            # Get numbers
            numbers = []
            print("Enter numbers (type 'done' when finished):")
            while True:
                user_input = input("Enter a number (or 'done' when finished): ")
                if user_input.lower() == 'done' and numbers:  # Ensure at least one number
                    break
                elif user_input.lower() == 'done':
                    print("You must enter at least one number.")
                    continue
                numbers.append(float(user_input))  # Convert input to float

            # Get operation
            op = input("Enter operation (+, -, *, /): ")
            
            # Calculate result
            if op not in ['+', '-', '*', '/']:
                print("Invalid operation. Please choose +, -, *, or /.")
                continue

            result = numbers[0]  # Start with first number
            if op == '+':
                for num in numbers[1:]:
                    result += num
            elif op == '-':
                for num in numbers[1:]:
                    result -= num
            elif op == '*':
                for num in numbers[1:]:
                    result *= num
            elif op == '/':
                division_by_zero = False
                for num in numbers[1:]:
                    if num == 0:
                        print("Cannot divide by zero.")
                        division_by_zero = True
                        break
                    result /= num
                if division_by_zero:
                    continue
                # Display result
                print(f"Result: {result}")
            else:
                # Display result for non-division operations
                print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        
        # Ask to continue or exit
        again = input("Calculate again? (yes/no): ")
        if again.lower() != 'yes':
            print("Goodbye!")
            break

# Run the calculator
if __name__ == "__main__":
    print("Welcome to the Calculator!")
    calculator()