#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import welcome


welcome()
name = welcome_user()[1]


def game_progression():
    print('What number is missing in the progression?')
    good_result = 0
    while good_result <= 3:
        stop = randint(20, 50)
        step = randint(1, 5)
        result = list(range(randint(0, 9), stop, step))[0: 5]
        answer = str(result[randint(0, 4)])
        result = " ".join(map(str, (result)))
        printer = result.replace(answer, "..", 1)
        print(f"Question: {printer}")
        answer_1 = prompt.integer('Your answer: ')
        if int(answer) != answer_1:
            return print(
                f"'{answer_1}' is wrong answer ;(. Correct answer was"
                f"\'{answer}\'."
                f"\nLet's try again, {name}!")
        else:
            print('Correct!')
            good_result += 1
            if good_result == 3:
                return print(f"Congratulations, {name}!")


def main():
    game_progression()


if __name__ == '__main__':
    main()
