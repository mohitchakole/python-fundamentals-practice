import random 
lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num,highest_num)

guesses = 0
is_running = True

print("Welcome to python number guessing game")
print(f"please select a number betwwen {lowest_num} and {highest_num}")

while is_running:
    guess = (input("enter your guess"))

    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess< lowest_num or guess>highest_num:
            print("that number is out of range")
            print(f"please select a number betwwen {lowest_num} and {highest_num}")
        elif guess<answer:
            print("Too low ! try again")
        elif guess>answer:
            print("Too high ! try again")
        else:
            print(f"corret the answer was {answer}")
            print(F"number of guesse :{guesses}")
    else:
        print("invalid guess")
        print(f"please select a number between {lowest_num} and {highest_num}")                