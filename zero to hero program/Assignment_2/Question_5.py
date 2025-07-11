# Write a Python program to convert height (in feet and inches) to centimeters


feet = int(input("Enter height (feet): "))
inches = int(input("Enter remaining inches: "))
centimeters= (feet * 12 + inches) * 2.54
print("Height in cm:", centimeters)