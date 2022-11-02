#!/usr/bin/env python3
import prompt
from brain_games.scripts.brain_games import welcome
from brain_games.cli import welcome_user


welcome()


def calc():
    name = welcome_user()[1]
    print('What is the result of expression?')
    print('Question: 4 + 10')
    answer1 = prompt.integer('Your answer: ')
    if answer1 != 14:
        print(f"'{answer1}' is wrong answer ;(. Correct answer was '14'.")
        return print(f"Let's try again, {name}!")
    print('Correct!\nQuestion: 25 - 11')
    answer2 = prompt.integer('Your answer: ')
    if answer2 != 14:
        print(f"'{answer2}' is wrong answer ;(. Correct was '14'.")
        return print(f"Let's try again, {name}!")
    print('Correct!\nQuestion: 25 * 7')
    answer3 = prompt.integer('Your answer: ')
    if answer3 != 175:
        print(f"'{answer3}' is wrong answer ;(. Correct was '175'.")
        return print(f"Let's try again, {name}!")
    print(f"Correct!\nCongratulations, {name}!")


def main():
    calc()


if __name__ == '__main__':
    main()
