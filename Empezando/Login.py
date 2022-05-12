password =  "password"

print(f"Password is: {password}, update please")

password = input("Create a password: ")
print("Welcome to the portal")

password_check = input("Please enter your password: ")

if password_check == password: #declaracion
    print("Welcome again")
else:
    print("I'm sorry friend! this is a Nay")