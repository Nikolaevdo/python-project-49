from operator import add, sub, mul
from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'
OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul
}


def make_question():
    first_number, second_number = randint(1, 50), randint(1, 50)
    operator = choice(list(OPERATORS.keys()))
    task = f"{first_number} {operator} {second_number}"
    correct_answer = str(eval(task))
    return correct_answer, task
