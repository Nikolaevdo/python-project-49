#!/usr/bin/env python3

from brain_games.cli import welcome_user, name

from random import randint
import prompt


def find_number():
    print('What number is missing in the progression?')
    correct_answers = 0

    while correct_answers < 3:
        number, step = randint(0, 50), randint(0, 50)
        sequence = [number + step * i for i in range(10)]
        random_index = randint(0, 9)
        correct_answer = str(sequence[random_index])
        sequence[random_index] = '..'

        print('Question:', *sequence)
        user_answer = prompt.string('Your answer:')

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f'{user_answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}.')
            break

    if correct_answers == 3:
        print(f'Congratulations, {name}!')


def main():
    welcome_user()
    find_number()


if __name__ == '__main__':
    main()
