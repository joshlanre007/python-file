#Write a program that simulates a login system with preset credentials (username and password)
#Correct username = joshlanre
#Correct password = 6789

username = input("Enter your username")
password = int(input("Enter your password"))
if username == "joshlanre" and password == 6789:
    print ("login successful. Welcome!")
else:
    print("login failed. incorrect username or password")