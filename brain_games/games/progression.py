from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def make_progression():
    start, step, length = randint(0, 50), randint(0, 50), 10
    end = start + length * step
    task = list(range(start, end, step))

    random_index = randint(0, 9)
    correct_answer = str(task[random_index])
    return task, correct_answer, random_index


def make_question():
    task, correct_answer, random_index = make_progression()
    task[random_index] = '..'
    task = ' '.join(str(i) for i in task)
    return correct_answer, task
