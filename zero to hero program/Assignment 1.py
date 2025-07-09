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
first_number = int(input("Enter the first side of the triangle: "))
second_number = int(input("Enter the second side of the triangle: "))

hypotenuse = (((first_number ** 2) + (second_number ** 2)) ** 0.5)

print(f'The hypotenuse of the right angled triangle is {hypotenuse}')


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

"""
#Prompt the user to enter their score and:
#print grade A (90-100), B (80-89), C (70-79), F (below 70)
"""

Score = int(input("Enter your score: "))

if Score >= 90 and Score <= 100:
    print(f'Grade A')

elif Score >= 80 and Score <= 89:
    print(f'Grade B')

elif Score >= 70 and Score <= 79:
    print(f'Grade C')

else:
    print(f'Grade F')

"""
 #Write a Python program to parse a string to float or integer.
 """

enter_value = float(input("Enter a number: "))

print(enter_value) #This will automatically convert the input to float if it contains a decimal point.
print(type(enter_value)) #This will show the datatype of the variable

"""
# Write a program that asks for the user's name and their favorite color
# Then,use string interpolation to create a personalized greeting
"""

name = input("Enter your name: ")
favourite_color = input("Enter your favourite color: ")
print(f'Hello {name}, your favourite color is {favourite_color}!')

"""
#write a Python program to check if a triangle is equilateral, isosceles or scalene.Note :
#An equilateral triangle is a triangle in which all three sides are equal.
#A scalene triangle is a triangle that has three unequal sides.
#An isosceles triangle is a triangle with (at least) two equal sides
"""

# Input sides
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

def triangle_type(a, b, c):
    # Check if it's a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a valid triangle!"
    
    # Check the type
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

# Get and print the result
result = triangle_type(a, b, c)
print(f"The triangle is: {result}")

"""
#Write a Python program that reads two integers representing a month andday and prints the season for that month and day.
#Expected Output:
#Input the month (e.g. January, February etc.): july
#Input the day: 31
#Season is harmattan
"""
def get_season(month, day):
    if month in ["April", "May", "June", "July", "August", "September"]:
        return 'Rainy Season'
    elif month in ["November", "December", "January", "February", "March"]:
        return 'Harmattan (Dry Season)'
    elif month == "October":
        return 'Transition (End of Rainy Season)'
    else:
        return 'Invalid month'

# Input and execution (outside the function!)
month = input("Input the month (e.g. January, February etc.): ").strip().title()  # .title() for consistency
day = int(input("Input the day: "))

season = get_season(month, day)
print(f'Season is {season}')

