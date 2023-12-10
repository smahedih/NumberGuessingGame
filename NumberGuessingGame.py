from random import randint

guessingNumber = int(input("Enter your guessing number between 1 and 10: "))
randomNumber = randint(1, 11)

if guessingNumber == randomNumber:
    print("Hurrah! You won.")
else:
    print("Oops! You lost.")
    print("Random number was: ", randomNumber)
