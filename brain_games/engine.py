import prompt

COUNTER_GAME_LOOP = 3


def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run_game(game):
    name = greet()
    print(game.DESCRIPTION)

    for counter in range(COUNTER_GAME_LOOP):
        correct_answer, task = game.make_question()
        print(f'Question: {task}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.'
                  f"\nLet's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
