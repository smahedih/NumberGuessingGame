from random import randint

guessingNumber = int(input("Enter your guessing number between 1 and 10: "))

# Check if input is out of range
if guessingNumber < 1 or guessingNumber > 10:
    print("Error: Number is out of range. Please enter a number between 1 and 10.")
else:
    randomNumber = randint(1, 10)

    if guessingNumber == randomNumber:
        print("Hurrah! You won.")
    else:
        print("Oops! You lost.")
        print("Random number was:", randomNumber)
