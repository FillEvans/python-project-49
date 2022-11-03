#!/usr/bin/env python3
import prompt
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import welcome


welcome()


def gcd():
    name = welcome_user()[1]
    print('Find the greatest common divisor of given numbers.')
    print('Question: 25 50')
    answer_1 = prompt.integer('Your answer: ')
    if answer_1 != 25:
        print(f"'{answer_1}' is wrong answer ;(. Correct answer was '25'.")
        return print(f"Let's try again, {name}!")
    print('Correct!\nQuestion: 100 52')
    answer_2 = prompt.integer('Your answer: ')
    if answer_2 != 4:
        print(f"'{answer_2}' is wrong answer ;(. Correct answer was '4'.")
        return print(f"Let's try again, {name}!")
    print('Correct!\nQuestion: 3 9')
    answer_3 = prompt.integer('Your answer: ')
    if answer_3 != 3:
        print(f"'{answer_3}' is wrong answer ;(. Correct answer was '3'.")
        return print(f"Let's try again, {name}!")
    print(f"Correct!\nCongratulations, {name}!")


def main():
    gcd()


if __name__ == '__main__':
    main()
