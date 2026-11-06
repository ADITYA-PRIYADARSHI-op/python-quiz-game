import random

print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100")

secret = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Enter your guess: "))
    tries = tries + 1

    if guess < secret:
        print("Too low, try again")
    elif guess > secret:
        print("Too high, try again")
    else:
        print("You got it!")
        print("The number was", secret)
        print("You took", tries, "tries")
        break