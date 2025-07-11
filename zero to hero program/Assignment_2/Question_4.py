# Write a Python program to compute the future value of a specified principalamount, rate of interest, and number of years.
# calculate simple interest based on user input

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