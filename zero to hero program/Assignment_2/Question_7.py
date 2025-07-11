  # Write a Python program to calculate the hypotenuse of a right angled triangle

first_number = int(input("Enter the first side of the triangle: "))
second_number = int(input("Enter the second side of the triangle: "))

hypotenuse = (((first_number ** 2) + (second_number ** 2)) ** 0.5)

print(f'The hypotenuse of the right angled triangle is {hypotenuse}')
