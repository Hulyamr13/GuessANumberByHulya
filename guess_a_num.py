import random

print("Welcome to the number guessing game!")


def get_range(level):
    if level == 1:
        return (1, 100)
    elif level == 2:
        return (1, 200)
    elif level == 3:
        return (1, 300)
    else:
        return (1, 1000)


def play_game():
    level = 1
    max_level = 3
    min_number, max_number = get_range(level)
    computer_number = random.randint(min_number, max_number)
    num_guesses = 0

    while True:
        player_input = input(f'Guess the number ({min_number}-{max_number}): ')
        if not player_input.isdigit():
            print('Invalid input. Try again...')
            continue
        player_number = int(player_input)
        num_guesses += 1
        if player_number == computer_number:
            print(f'You guessed it in {num_guesses} tries!')
            response = input('Play again? (y/n): ')
            if response.lower() == 'y':
                level = 1
                min_number, max_number = get_range(level)
                computer_number = random.randint(min_number, max_number)
                num_guesses = 0
            else:
                print('Thanks for playing!')
                break
        elif player_number > computer_number:
            print('Too high!')
        else:
            print('Too low!')

        if num_guesses == 10:
            print(f'You reached the maximum number of tries. The number was {computer_number}.')
            response = input('Play again? (y/n): ')
            if response.lower() == 'y':
                level = 1
                min_number, max_number = get_range(level)
                computer_number = random.randint(min_number, max_number)
                num_guesses = 0
            else:
                print('Thanks for playing!')
                break

        if num_guesses % 5 == 0:
            level += 1
            if level > max_level:
                level = max_level
            min_number, max_number = get_range(level)
            print(f'Congratulations, you have reached Level {level}!')


play_game()