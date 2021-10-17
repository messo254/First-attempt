# Program make a simple calculator
# import the math package
import math
pi = math.pi

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function gets the modulus of a number
def modulo(x, y):
    return x % y

# This function gets the Area of a Circle
def CircleArea(x):
    return (pi * (x * x))

# This function gets the Circumference of a Circle
def CircleCircumference(x):
    return (2 * pi *  x)

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulo")
print("6: Area of a circle")
print("7. Circumference of a circle")
print("")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("The sum of", num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print("The difference of", num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print("The product of", num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print("The division of", num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print("The modulus of", num1, "%", num2, "=", modulo(num1, num2))

        elif choice == '6':
            print("The radius is", num1, "and the Circle Area", "=", CircleArea(num1))

        elif choice == '7':
            print("The radius is", num1, "and the Circle Circumference", "=", CircleCircumference(num1))
        break
    else:
        print("Invalid Input")