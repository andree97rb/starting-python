print("Welcome to our online eligibility checker")
age = int(input("Enter your age: "))
has_licence = input("Do you have a license? [Y/N]: ")

if has_licence.lower() == "y":
    has_licence = True
else:
    has_licence = False

salary = int(input("Your monthly salary is: $"))

if age <= 35:
    print("Age is fine!")
    if has_licence:
        print("You have a valid license")
        if salary >= 3500:
            print("Perfect! you are eligible")
        else:
            print("I'm sorry but you are below our minimum requirement")
    else:
        print("Sorry, but you need a valid license")
else:
    print("You are over our age limit")
