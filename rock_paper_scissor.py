import random

running= True

while running :
    options = ("rock","paper","scissor")
    player = None
    computer = random.choice(options)

    while player not in options:
        player=input("enter your choice(rock,paper,scissor)")
        print(f"player:{player}")
        print(f"Computer:{computer}")

    if player==computer:
        print("it's a tie")
    elif player=="rock" and computer=="scissor":
        print("you win!")
    elif player=="paper" and computer=="rock":
        print("you win!")
    elif player=="scissor" and computer=="paper":
        print("you win!")
    else:
        print("you lose!")

    play_again = input("play again? (Y/N) :").upper()
    if not play_again=="Y":
        running = false        
                


