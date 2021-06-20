# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art2 import logo
import random

print(logo)

print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty_level = input(
    "Choose a difficulty level. Type 'easy' or 'hard': ".lower())
num_attempts = 0
if difficulty_level == "easy":
    num_attempts += 10
    print(f"You have {num_attempts} attempts remaining to guess the number")
elif difficulty_level == "hard":
    num_attempts += 5
    print(f"You have {num_attempts} attempts remaining to guess the number")
# generating the random number
random_number = random.randint(1, 100)
# print(random_number)

your_guess = int(input("Make a guess: "))

is_game_over = False
while not is_game_over:
    if your_guess > random_number:
        num_attempts -= 1
        print(
            f"Too high.\nGuess again.\nYou have {num_attempts} attempts remaining to guess the number")
        your_guess = int(input("Make a guess: "))
    # if another_guess > random_number:
        #print(f"You have {num_attempts} attempts remaining to guess the number")
    if your_guess < random_number:
        num_attempts -= 1
        print(
            f"Too low.\nGuess again.\nYou have {num_attempts} attempts remaining to guess the number")
        your_guess = int(input("Make a guess: "))
    # if another_guess < random_number:
        # print(f"You have {num_attempts} attempts #remaining to guess the number")
    if your_guess == random_number:
        is_game_over = True
        print("You guessed the right number.You win!")
    if num_attempts == 0:
        is_game_over = True
        print(f"The right number is {random_number}")
        print("You have run out of attempts. Game Over...")
