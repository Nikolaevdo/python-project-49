#!/usr/bin/env python3


from brain_games.cli import welcome_user, name
from random import randint
import prompt

BRAIN_PRIME_TEXT = "Answer \"yes\" if given number is prime. " \
                   "Otherwise answer \"no\"."


def is_prime(value):
    if value <= 1:
        return "no"
    for i in range(2, value):
        if value % i == 0:
            return "no"
    return "yes"


def main():
    welcome_user()
    counter = 0
    while counter < 3:
        number = randint(1, 100)
        print(BRAIN_PRIME_TEXT)
        print(f"Question : {number}")
        user_answer = prompt.string()
        correct_answer = is_prime(number)
        print(f"Your answer : {user_answer}")
        if user_answer == correct_answer:
            counter += 1
            print("Correct!")
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.'
                  f"\nLet's try again, {name}!")
            return
    if counter == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
