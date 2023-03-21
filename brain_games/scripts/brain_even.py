#!/usr/bin/env python
""" The essence of the game is as follows: the user is shown a
 random number.And he needs to answer
 yes if the number is even, or no if it is odd
 If the user gives an incorrect answer, it is necessary to end the
 game and display a message:
 'yes' is wrong answer ;(. Correct answer was 'no'.
 Let's try again, Bill!
 If the user entered the correct answer, you need to display:
 Correct!
 and move on to the next number.
 The user must give the correct answer to three questions in a row.
  After a successful game, you need to output:
 Congratulations, Bill"""

from random import randint
from brain_games.cli import welcome_user, name

GAME_EVEN_QUEST = 'Answer "yes" if the number is even, otherwise answer "no".'


def console_input():
    user_io = input()
    if len(user_io) >= 2:
        return user_io
    else:
        print("Your answer is too short. Please try again.")
        return console_input()


def parity_check():
    welcome_user()
    print(GAME_EVEN_QUEST)

    counter = 0
    while counter < 3:
        mystery_number = randint(1, 100)
        print(f"Question: {mystery_number}")
        user_input = console_input()
        print(f"Your answer: {user_input}")
        if (mystery_number % 2 == 0 and user_input == 'yes') \
                or (mystery_number % 2 != 0 and user_input == 'no'):
            print('Current!')
            counter += 1
        else:
            print(f'''Wrong answer! Better luck next time
                Let's try again, {name()}!''')
            parity_check()


print(f'Congratulations, {name}!')


def main():
    parity_check()


if __name__ == '__main__':
    main()
