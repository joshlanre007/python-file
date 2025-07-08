
import math

def find_lcm(x, y):
    # The LCM of two numbers is their product divided by their GCD
    return abs(x * y) // math.gcd(x, y)

# Prompt the user to enter two positive integers
try:
    num1 = int(input("Enter the first positive integer: "))
    num2 = int(input("Enter the second positive integer: "))

    if num1 <= 0 or num2 <= 0:
        print("Please enter positive integers only.")
    else:
        lcm = find_lcm(num1, num2)
        print(f"The Least Common Multiple of {num1} and {num2} is {lcm}.")
except ValueError:
    print("Invalid input! Please enter valid integers.")