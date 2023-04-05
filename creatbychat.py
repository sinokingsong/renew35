import random

number = random.randint(1, 100)
guesses_left = 10

print("I am thinking of a number between 1 and 100. You have 10 guesses to get it right.")

while guesses_left > 0:
    guess = int(input("Guess a number: "))
    guesses_left -= 1

    if guess == number:
        print("Congratulations! You guessed the number in {} guesses.".format(10 - guesses_left))
        break
    elif guess < number:
        print("Too low. Guesses left: {}".format(guesses_left))
    else:
        print("Too high. Guesses left: {}".format(guesses_left))

print("The number was {}".format(number))
