#Create a simple login system. Define a username and password in yourcode.
# # Ask the user to enter their username and password.
#  #If they match thepredefined credentials, print "Login successful." Otherwise, print "Invalidcredentials.



# Predefined credentials
correct_username = "joshlanre Stores"
correct_password = "peace444"

# Ask user to enter login info
entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

# Check credentials
if entered_username == correct_username and entered_password == correct_password:
    print("Login successful.")
else:
    print("Invalid credentials.")