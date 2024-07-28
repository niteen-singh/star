# Rock Paper Scissors
import random

options = ("rock", "paper", "scissors")

running = True

while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Choose rock, paper, or scissors: ")

    print(f"player choice: {player}")
    print(f"computer choice: {computer}")

    if player == computer:
        print("It's a tie!")
    elif ((player == "rock" and computer == "scissors") or
          (player == "paper" and computer == "rock") or
          (player == "scissors" and computer == "paper")):
        print("you won!")
    else:
        print("you lost!")

    if not input("Enter (y/n) to play again: ").lower() == "y":
        running = False

print("Thanks for playing!")