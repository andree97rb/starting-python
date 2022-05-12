#attempts = 3
#secret_number = input("Enter a number: ")

#while attempts > 1 :#3

#    if secret_number != 19:
#        attempts -= 1
#        print(f"Try again, you have {attempts} chances left")
#        secret_number = input("Enter a number: ")
#    else:
#        print("You win")
#        break
#print("Game over)

my_number = 19
guess = 0
max_guess= 3

while guess < max_guess:
    number = int(input("Guess the number: "))
    guess += 1
    if number == my_number:
        print("woow, genius")
        break
    else:
        print("Do not! Not in a million years! Try again!")
else:
    print("your chances are over")