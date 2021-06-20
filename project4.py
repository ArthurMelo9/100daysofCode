import random

print ("Welcome to Rock, Paper , Scissors!")
player_choice= input("Type 0 for Rock, 1 for Paper and 2 for Scissors-  ")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#player choices
if player_choice=="0":
    print(rock)
elif player_choice=="1":
    print(paper)
elif player_choice=="2":
    print(scissors)

#computer choices
com_choice= random.randint(0,2)
if com_choice==0:
    print(rock)
elif com_choice==1:
    print(paper)
elif com_choice==2:
    print(scissors)

#rules of the game
#wins
if player_choice=="0" and com_choice==2:
    print("You win!")
elif player_choice=="1" and com_choice==0:
    print("You win!")
elif player_choice=="2" and com_choice==1:
    print("You win!")
#losses
elif player_choice=="0" and com_choice==1:
    print("You lose.")
elif player_choice=="1" and com_choice==2:
    print("You lose.")
elif player_choice=="2" and com_choice==0:
    print("You lose")
else:
    print("Draw")