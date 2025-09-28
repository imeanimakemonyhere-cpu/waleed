def calculator():
    while True:
        print("\n***Calculator***")
        print("1. addition (+)")
        print("2. substraction (-)")
        print("3. multiplication (*)")
        print("4. division (/)")
        print("5. Exit ")
        choice = input("Enter Your choice (1-5): ")

        if choice == "5":
           print("Eixitting...")
           break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if choice == "1":
            print(f"result : {num1 + num2}")
        elif choice == "2":
            print(f"result : {num1 - num2}")
        elif choice == "3":
            print(f"result : {num1 * num2}")
        elif choice == "4":
            if num1 != 0:
                print(f"result : {num1 / num2}")
            else:
                print("Error... cannot divide by zero")
        else:
            print("invalid choice please try (1-5)")

calculator()
print()


