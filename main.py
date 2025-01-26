# Importing the add function from addition.py
from addition import add
from substraction import sub
from multiplication import mul
from division import div

def main():
    print("Welcome to the Calculator!")
    print("1. Addition")
    print('2. Substraction')
    print('3 Multiplication')
    print('4. Division')

    # Get user choice
    choice = input("Enter your choice (1 for Addition, 2 for Substraction 3 for multiplication): ")

    if choice == '1':
        # Get user input for numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Perform addition
            result = add(num1, num2)
            print(f"The result of addition is: {result}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    elif choice == '2':
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Perform addition
            result = sub(num1, num2)
            print(f"The result of substraction is: {result}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    elif choice == '3':
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Perform multiplication
            result = mul(num1, num2)
            print(f"The result of multiplication is: {result}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    elif choice == '4':
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Perform division
            result = div(num1, num2)
            print(f"The result of div is: {result}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()