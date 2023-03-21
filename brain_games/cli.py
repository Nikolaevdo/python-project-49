#!/usr/bin/env python
"""Welcome user script."""
import prompt

name = prompt.string('May I have your name? ')


def welcome_user():
    """Get name and greeting to user."""

    print('Hello, {0}!'.format(name))


if __name__ == '__main__':
    welcome_user()


def name():
    return name()
