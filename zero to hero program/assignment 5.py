# A shop offers a 10% discount if the total bill is over $100.
# Write a programthat asks for the total bill amount and
# prints the final amount to be paid after the discount

total_bill = float(input("Enter the total bill amoumt: #"))

# Check if the bill qualifies for a discount
if total_bill > 100:
    discount = total_bill * 0.10
    final_amount = total_bill - discount
    print(f"A 10% discount applies. Final amount to be paid: #{final_amount:.2f}")
else:
    final_amount = total_bill
    print(f"No discount applies. Final amount to be paid: #{final_amount:.2f}")