#son of a gun code. well guys this is me 😁✌🏼...


import math 

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input.please enter a number.")
    
def calculator():
    print("Advanced Calculator")
    print("=" * 30)

    while True:
        print("\nOperations:")
        print("1. Add (+)")
        print("2. Sustract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Power (^)")
        print("6. Square Root (√)")
        print("7. Modulo (%)")
        print("8. Exit")
        
        choice = input("\nEnter choice (1-7): ").strip()

        if choice == "8":
            print("Goodbye.")
            break

        if choice in ['1', '2', '3', '4', '5','7']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
        elif choice == "6":
            num1 = get_number("Enter number: ")
        else:
            print(("Invalid choice.Please select 1-8."))
            continue

        if choice == "1":
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == "2":
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == "3":
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == "4":
            if num2 == 0:
                print("Error: cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        elif choice == "5":
            result = num1 ** num2 
            print(f"Result: {num1} ^ {num2} = {result}") 
        elif choice == "6":
            if num1 < 0:
                print("Error: cannot take square root of a negative number.")
            else:
                result = math.sqrt(num1)
                print(f"Result: √{num1} = {result}")
        elif choice == "7":
            if num2 == 0:
                print("Error: cannot modulo by zero.")
            else:
                result = num1 % num2
                print(f"Result: {num1} % {num2} = {result}")
        print("-" * 30)
    
if __name__ == "__main__":
    calculator()

