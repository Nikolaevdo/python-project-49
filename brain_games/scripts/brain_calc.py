#!/usr/bin/env python
"""
The essence of the game is as follows: the user is shown a random mathematical expression,
for example 35 + 16, which must be calculated and the correct answer written down.
"""

from random import randint, choice
from brain_games.cli import welcome_user, name

# The question text
GAME_CALC_TEXT = "What is the result of the expression?"


def main():
    welcome_user()

    # Counter for correct answers
    counter = 0
    # Available operators
    operators = ['+', '-', '*']
    while counter < 3:
        num1, num2 = randint(1, 100), randint(1, 100)
        operator = choice(operators)
        print(GAME_CALC_TEXT)
        print(f'Question: {num1} {operator} {num2}')
        # Calculation of the correct answer
        task_value = eval(f"{num1} {operator} {num2}")
        user_input = input("Your answer: ")
        if int(user_input) == task_value:
            # Incrementing the counter on correct answer
            counter += 1
            print("Correct!")
        else:
            print(f"\'{user_input}\' is wrong answer ;(. Correct answer was \'{task_value}\'.")
            print(f"Let's try again, {name}!")
            # Exiting the game on incorrect answer
            return

            # Congratulating the user after three correct answers
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
