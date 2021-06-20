print("Welcome to Arthurland")
print("Your job is to find the treasure")

first_step = input("Where do you want to turn? left or right? ").lower()
if first_step == "left":
    second_step = input("You get to a lake. will you swim across or walk to the other side of the lake? walk or swim? ").lower()
    if second_step == "swim":
        third_step = input("At the other side of the lake, there are three doors- green, blue and yellow. Choose...")
        if third_step == "yellow":
            print("Congratulaions! You discovered the treasure!")
        elif third_step =="blue":
            print("Game over! You fell off a cliff")
        elif third_step == "green":
            print("Game over! You git entangled in thorns and thistles")
    else:
        print("Game over! You got devoured by wild land animals")
else:
    print("Game over! You fell into a ditch")