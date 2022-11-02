#!/usr/bin/env python3
import prompt
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import welcome


welcome()


def gcd():
    name = welcome_user()[1]
    print('Find the greatest common divisor of given numbers.')
    print('Question: 25 50')
    answer1 = prompt.integer('Your answer: ')
    if answer1 != 25:
        print(f"'{answer1}' is wrong answer ;(. Correct answer was '25'.")
        return print(f"Let's try again, {name}!")
    print('Correct!\nQuestion: 100 52')
    answer2 = prompt.integer('Your answer: ')
    if answer2 != 4:
        print(f"'{answer2}' is wrong answer ;(. Correct answer was '4'.")
        return print(f"Let's try again, {name}!")
    print('Correct!\nQuestion: 3 9')
    answer3 = prompt.integer('Your answer: ')
    if answer3 != 3:
        print(f"'{answer3}' is wrong answer ;(. Correct answer was '3'.")
        return print(f"Let's try again, {name}!")
    print(f"Correct!\nCongratulations, {name}!")


def main():
    gcd()


if __name__ == '__main__':
    main()
