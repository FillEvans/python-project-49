#!/usr/bin/env python3
import prompt
import math
import random
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import welcome


welcome()
name = welcome_user()[1]


def game_gcd():
    print('Find the greatest common divisor of given numbers.')
    good_result = 0
    while good_result <= 3:
        num_1 = random.randint(1, 50)
        num_2 = random.randint(1, 50)
        print(f"Question: {num_1} {num_2}")
        answer = prompt.integer('Your answer: ')
        result = math.gcd(num_1, num_2)
        if answer != result:
            return print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{result}'"
                f"\nLet's try again, {name}!")
        good_result += 1
        print('Correct!')
        if good_result == 3:
            return print(f"Congratulations, {name}!")


def main():
    game_gcd()


if __name__ == '__main__':
    main()
