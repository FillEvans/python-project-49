#!/usr/bin/env python3
import prompt
from brain_games.scripts.brain_games import welcome
from brain_games.cli import welcome_user
import random


welcome()
name = welcome_user()[1]


def calc():
    calc = ["+", "-", "*"]
    num_1 = random.randint(1, 50)
    num_2 = random.randint(1, 50)
    operator = random.choice(calc)
    if operator == '+':
        result = num_1 + num_2
    elif operator == '-':
        result = num_1 - num_2
    elif operator == '*':
        result = num_1 * num_2
    return [result, num_1, num_2, operator]


def game_calc():
    print('What is the result of the expression?')
    good_result = 0
    while good_result <= 3:
        result, num_1, num_2, operator = calc()
        print(f'Question: {num_1} {operator} {num_2}')
        answer = prompt.string('Your answer: ')
        if str(result) == str(answer):
            print("Correct!")
            good_result += 1
            if good_result == 3:
                return print(f"Congratulations, {name}!")
        else:
            print(
                f"'answer' is wrong answer ;(. Correct answer was '{result}'.")
            return print(f"\nLet's try again, {name}!")


def main():
    game_calc()


if __name__ == '__main__':
    main()
