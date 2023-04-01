import random

MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_TRIES = 5

print("Welcome to the number guessing game!")
print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}. Can you guess it in {MAX_TRIES} tries?")

secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)

for guess_count in range(1, MAX_TRIES + 1):
    guess = input(f"Guess #{guess_count}: ")

    if not guess.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    guess = int(guess)

    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {guess_count} tries!")
        break
    elif guess < secret_number:
        print("Too low! Guess again.")
    else:
        print("Too high! Guess again.")
else:
    print(f"Sorry, you didn't guess the number. It was {secret_number}. Better luck next time!")
