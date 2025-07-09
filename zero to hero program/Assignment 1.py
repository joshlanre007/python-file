"""
#Write a program that simulates a login system with preset credentials (username and password)
#Correct username = joshlanre
#Correct password = 6789
"""

username = input("Enter your username")
password = int(input("Enter your password"))
if username == "joshlanre" and password == 6789:
    print ("login successful. Welcome!")
else:
    print("login failed. incorrect username or password") 


    """
    #Write a Python program that calculates the area of a circle based on the radius entered by the user
#Sample Output :
#r = 1.1
#Area = 3.801327110843650
"""

r = float(input("Enter the radius of the circle: "))
area = 3.142 * r ** 2
print("r =", r)
print("Area =", area)


"""
# A shop offers a 10% discount if the total bill is over $100.
# Write a programthat asks for the total bill amount and
# prints the final amount to be paid after the discount
"""

total_bill = float(input("Enter the total bill amoumt: #"))

# Check if the bill qualifies for a discount
if total_bill > 100:
    discount = total_bill * 0.10
    final_amount = total_bill - discount
    print(f"A 10% discount applies. Final amount to be paid: #{final_amount:.2f}")
else:
    final_amount = total_bill
    print(f"No discount applies. Final amount to be paid: #{final_amount:.2f}")

"""
# Write a Python program to compute the future value of a specified principalamount, rate of interest, and number of years.
# calculate simple interest based on user input
"""
# Get user input
principal = float(input("Enter the principal amount: #"))
rate = float(input("Enter the annual interest rate (in %): "))
years = float(input("Enter the number of years: "))

# Calculate simple interest
simple_interest = (principal * rate * years) / 100
future_value = principal + simple_interest

# Display the result
print(f"Simple Interest: #{simple_interest:.2f}")
print(f"Future Value after {years} years: #{future_value:.2f}")


"""
# Write a Python program to convert height (in feet and inches) to centimeters
"""

feet = int(input("Enter height (feet): "))
inches = int(input("Enter remaining inches: "))
centimeters= (feet * 12 + inches) * 2.54
print("Height in cm:", centimeters)

"""
# Write a Python program to find the least common multiple (LCM) of two positive integers
# enter by the user from the termina
"""
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

    """
    # Write a Python program to calculate the hypotenuse of a right angled triangle
"""
import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

try:
    side_a = float(input("Enter the length of the first leg (a): "))
    side_b = float(input("Enter the length of the second leg (b): "))

    if side_a <= 0 or side_b <= 0:
        print("Both side lengths must be positive numbers.")
    else:
        hypotenuse = calculate_hypotenuse(side_a, side_b)
        print(f"The length of the hypotenuse is: {hypotenuse:.2f}")
except ValueError:
    print("Invalid input! Please enter valid numerical values.")


    """
# Prompt for a number. Print whether it's Positive Negative Zero
    """
    
number = int(input("Enter any number: "))

if number > 0:
    print(f'The number is postive: {number}')

elif number == 0:
    print(f'The number is Zero: {number}')

else:
    print(f'The number is negative {number}')
