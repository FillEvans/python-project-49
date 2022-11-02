#!/usr/bin/env python3
import prompt
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main

main()
# welcome_user()


def is_even():
    print('Answer "yes" if the number is even, otherwise answer "no".\nQuestion: 15')
    answer1 = prompt.string('Your answer: ')
    if answer1 != 'no':
        return print(f"{answer1} is wrong answer ;(. Correct answer was 'no'\nLet's try again, {name}")
    print('Correct!\nQuestion: 6')
    answer2 = prompt.string('Your answer: ')
    if answer2 != 'yes':
        return print(f"{answer2} is wrong answer ;(. Correct answer was 'yes'\nLet's try again, {name}")
    print('Correct!\nQuestion: 7')
    answer3 = prompt.string('Your answer: ')
    if answer3 != 'no':
        return print(f"{answer3} is wrong answer ;(. Correct answer was 'no'\nLet's try again, {name}")
    print(f'Correct!\nCongratulations, {name}')


is_even()