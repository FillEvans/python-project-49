#!/usr/bin/env python3
from brain_games.cli import welcome_user
import prompt
from brain_games.scripts.brain_games import welcome


welcome()


def is_even():
    name = welcome_user()[1]
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print('Question: 15')
    answer_1 = prompt.string('Your answer: ')
    if answer_1 != 'no':
        print(f"'{answer_1}' is wrong answer ;(. Correct answer was 'no'.")
        return print(f"Let's try again, {name}!")
    print('Correct!\nQuestion: 6')
    answer_2 = prompt.string('Your answer: ')
    if answer_2 != 'yes':
        print(f"'{answer_2}' is wrong answer ;(. Correct answer was 'yes'.")
        return print(f"Let's try again, {name}!")
    print('Correct!\nQuestion: 7')
    answer_3 = prompt.string('Your answer: ')
    if answer_3 != 'no':
        print(f"'{answer_3}' is wrong answer ;(. Correct answer was 'no'.")
        return print(f"Let's try again, {name}!")
    print(f'Correct!\nCongratulations, {name}!')


def main():
    is_even()


if __name__ == '__main__':
    main()
