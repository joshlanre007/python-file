#simulate a simple ATM.
#Initialize a balance, say $1000.
#Ask the user what they want to do: 'withdraw', 'deposit', or 'check balance'.
#If they choose 'withdraw', ask for the amount and subtract it from the balance,
#but only if they have enough funds.
#If they choose 'deposit', ask for the amount and add it to the balance.
#If they choose 'check balance', display the current balance.
#Handle invalid input gracefull



# Initial balance
balance = 1000.0

# Display options
print("Welcome to the ATM!")
print("Options: 'withdraw', 'deposit', 'check balance'")

# Get user choice
action = input("What would you like to do? ").strip().lower()

# Handle user action
if action == "withdraw":
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print(f"Withdrawal successful. New balance: ${balance:.2f}")

elif action == "deposit":
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print(f"Deposit successful. New balance: ${balance:.2f}")

elif action == "check balance":
    print(f"Your current balance is: ${balance:.2f}")

else:
    print("Invalid input. Please select a valid option.")