#!/usr/bin/env python3
import prompt
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import welcome
from random import randint
from math import sqrt

welcome()
name = welcome_user()[1]


def is_prime(n):
    prime = True
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            prime = False
            break
        i += 1
    if prime:
        return True
    else:
        return False


def prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    good_result = 0
    while True:
        primer = randint(1, 100)
        print(f'Question: {primer}')
        answer = prompt.string('Your answer: ')
        if is_prime(primer):
            if answer != 'yes':
                print(f"'{answer}' is wrong answer ;(. Correct was 'yes'.")
                return print(f"Let's try again, {name}!")
            print('Correct!')
            good_result += 1
            if good_result == 3:
                return print(f"Congratulations, {name}!")
        elif is_prime(primer) is False:
            if answer != 'no':
                print(f"'{answer}' is wrong answer ;(. Correct was 'no'.")
                return print(f"Let's try again, {name}!")
            print('Correct!')
            good_result += 1
            if good_result == 3:
                return print(f"Congratulations, {name}!")


def main():
    prime()


if __name__ == '__main__':
    main()
