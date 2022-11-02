#!/usr/bin/env python3
import prompt
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import welcome


welcome()


def progression():
    name = welcome_user()[1]
    print('What number is missing in the progression?')
    print('Question: 5 7 9 11 13 .. 17 19 21 23')
    answer1 = prompt.integer('Your answer: ')
    if answer1 != 15:
        print(f"'{answer1}' is wrong answer ;(. Correct answer was '15'.")
        return print(f"Let's try again, {name}!")
    print('Correct!\nQuestion: 2 5 8 .. 14 17 20 23 26 29')
    answer2 = prompt.integer('Your answer: ')
    if answer2 != 11:
        print(f"'{answer2}' is wrong answer ;(. Correct answer was '11'.")
        return print(f"Let's try again, {name}!")
    print('Correct!\nQuestion: 14 19 24 29 34 39 44 49 54 ..')
    answer3 = prompt.integer('Your answer: ')
    if answer3 != 59:
        print(f"'{answer3}' is wrong answer ;(. Correct answer was '59'.")
        return print(f"Let's try again, {name}!")
    print(f"Correct!\nCongratulations, {name}!")


def main():
    progression()


if __name__ == '__main__':
    main()
