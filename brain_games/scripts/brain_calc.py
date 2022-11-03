#!/usr/bin/env python3
import prompt
from brain_games.scripts.brain_games import welcome
from brain_games.cli import welcome_user


welcome()


def calc():
    name = welcome_user()[1]
    print('What is the result of expression?')
    print('Question: 4 + 10')
    answer_1 = prompt.integer('Your answer: ')
    if answer_1 != 14:
        print(f"'{answer_1}' is wrong answer ;(. Correct answer was '14'.")
        return print(f"Let's try again, {name}!")
    print('Correct!\nQuestion: 25 - 11')
    answer_2 = prompt.integer('Your answer: ')
    if answer_2 != 14:
        print(f"'{answer_2}' is wrong answer ;(. Correct was '14'.")
        return print(f"Let's try again, {name}!")
    print('Correct!\nQuestion: 25 * 7')
    answer_3 = prompt.integer('Your answer: ')
    if answer_3 != 175:
        print(f"'{answer_3}' is wrong answer ;(. Correct was '175'.")
        return print(f"Let's try again, {name}!")
    print(f"Correct!\nCongratulations, {name}!")


def main():
    calc()


if __name__ == '__main__':
    main()
