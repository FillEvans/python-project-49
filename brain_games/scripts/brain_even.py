#!/usr/bin/env python3
from brain_games.cli import welcome_user
import prompt
from brain_games.scripts.brain_games import welcome


welcome()


def is_even():
    name = welcome_user()[1]
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print('Question: 15')
    answer1 = prompt.string('Your answer: ')
    if answer1 != 'no':
        print(f"'{answer1}' is wrong answer ;(. Correct answer was 'no'.")
        return print(f"Let's try again, {name}!")
    print('Correct!\nQuestion: 6')
    answer2 = prompt.string('Your answer: ')
    if answer2 != 'yes':
        print(f"'{answer2}' is wrong answer ;(. Correct answer was 'yes'.")
        return print(f"Let's try again, {name}!")
    print('Correct!\nQuestion: 7')
    answer3 = prompt.string('Your answer: ')
    if answer3 != 'no':
        print(f"'{answer3}' is wrong answer ;(. Correct answer was 'no'.")
        return print(f"Let's try again, {name}!")
    print(f'Correct!\nCongratulations, {name}!')


def main():
    is_even()


if __name__ == '__main__':
    main()
