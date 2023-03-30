#!/usr/bin/env python3

from brain_games.cli import welcome_user, name
from random import randint

GAME_EVEN_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_user_input():
    """Function to get user input and check if it's valid"""
    user_io = input()
    # Checking if user input is too short
    if len(user_io) >= 2:
        return user_io
    else:
        print("Your answer is too short. Please try again.")
        return get_user_input()


def parity_check():
    """Function to check if number is even and get user input"""
    welcome_user()
    print(GAME_EVEN_TEXT)

    # Counter for correct answers
    counter = 0
    while counter < 3:
        mystery_number = randint(1, 100)
        print(f"Question: {mystery_number}")
        user_input = get_user_input()
        print(f"Your answer: {user_input}")
        if (mystery_number % 2 == 0 and user_input == 'yes') \
                or (mystery_number % 2 != 0 and user_input == 'no'):
            print('Correct!')
            counter += 1  # Incrementing counter on correct answer
        else:
            print(f"Wrong answer! Let's try again, {name}!")
            # Calling the function recursively on incorrect answer
            return
            # Congratulating the user after three correct answers
    print(f'Congratulations, {name}!')


def main():
    parity_check()


if __name__ == '__main__':
    main()
