#!/usr/bin/env python
"""
The essence of the game is as follows: the user is shown a random mathematical expression,
for example 35 + 16, which must be calculated and the correct answer written down.
"""

from random import randint, choice

GAME_CALC_TEXT = "What is the result of the expression?"  # The question text


def welcome_user():
    """Function to greet the user and request their name"""
    print("Welcome to the game!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def main():
    name = welcome_user()
    counter = 0  # Counter for correct answers
    operators = ['+', '-', '*']  # Available operators
    while counter < 3:
        num1, num2 = randint(1, 100), randint(1, 100)
        operator = choice(operators)
        print(GAME_CALC_TEXT)
        print(f'Question: {num1} {operator} {num2}')
        task_value = eval(f"{num1} {operator} {num2}")  # Calculation of the correct answer
        user_input = input("Your answer: ")
        if int(user_input) == task_value:
            counter += 1  # Incrementing the counter on correct answer
            print("Correct!")
        else:
            print(f"\'{user_input}\' is wrong answer ;(. Correct answer was \'{task_value}\'.")
            print(f"Let's try again, {name}!")
            return  # Exiting the game on incorrect answer
    print(f"Congratulations, {name}!")  # Congratulating the user after three correct answers


if __name__ == '__main__':
    main()
