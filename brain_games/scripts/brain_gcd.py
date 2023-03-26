#!/usr/bin/env python3
import prompt

from brain_games.cli import welcome_user, name
from random import randint
from math import gcd

BRAIN_GCD_TEXT = "Find the greatest common divisor of given numbers."


def random_even_number(start, end):
    """ generate random number in sunlight
     from start to finish and multiply by 2 to get an even number """

    num = randint(start // 2, end // 2) * 2
    return num


def main():
    welcome_user()
    counter = 0
    while counter < 3:
        print(BRAIN_GCD_TEXT)
        num1 = random_even_number(2, 100)
        num2 = random_even_number(2, 100)
        print(f"Question : {num1}  {num2}")
        correct_answer = str(gcd(num1, num2))
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.'
                  f"\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
