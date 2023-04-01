import random

WORDS = [ 'Cat', 'Dog', 'Mouse', 'Horse', 'Bird', 'apple', 'banana', 'cherry',
          'dragonfruit', 'elderberry', 'fig', 'grapefruit', 'honeydew', 'jackfruit']

MAX_TRIES = 7

print("Welcome to the word guessing game!")
print(f"I'm thinking of a fruit name. Can you guess it in {MAX_TRIES} tries?")

secret_word = random.choice(WORDS)

for guess_count in range(1, MAX_TRIES + 1):
    guess = input(f"Guess #{guess_count}: ")

    if not guess.isalpha():
        print("Invalid input. Please enter a single word.")
        continue

    if guess.lower() == secret_word:
        print(f"Congratulations! You guessed the word '{secret_word}' in {guess_count} tries!")
        break
    else:
        print("Wrong! Guess again.")
else:
    print(f"Sorry, you didn't guess the word. It was '{secret_word}'. Better luck next time!")