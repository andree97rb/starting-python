print("Welcome to my little game")
number = int(input("Choose a number between 1-3: "))

if number == 1:
    print("You love to think of yourself as a leader")
    number2 = float(input("Enter a number with a decimal place between 1 and 2:"))
    if number2 == 2.00:
        print("It's okay! I meant a little less than that")
    elif number2 == 1.50:
        print("Oh come on, you can go higher!")
    else:
        print("It doesn't matter, forget")
elif number==2:
    print("You hate being alone, right?")
elif number==3:
    print("How much more is better, right?")
else:
    print("Really? You can't follow simple instructions, can you?")