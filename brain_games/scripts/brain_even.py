#!/usr/bin/env python3
from brain_games.cli import welcome_user
import prompt
from random import randint
from brain_games.scripts.brain_games import welcome


welcome()
name = welcome_user()[1]


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def game_is_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    good_result = 0
    while True:
        primer = randint(1, 20)
        print(f"Question: {primer}")
        answer = prompt.string('Your answer: ')
        if is_even(primer) and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            return print(f"\nLet's try again, {name}!")
        elif is_even(primer) is False and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            return print(f"\nLet's try again, {name}!")
        print('Correct!')
        good_result += 1
        if good_result == 3:
            return print(f"Congratulations, {name}!")


def main():
    game_is_even()


if __name__ == '__main__':
    main()
