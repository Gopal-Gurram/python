import sys

from random import randint

random_number = randint(1, 10)

while True:
    try:
        guess = int(input("Please enter a random number between 1~10:   "))

        if 0 < guess < 11:
            if guess == random_number:
                print('You are a genius')
                break
        else:
            print('hey bozo, I said 1 ~ 10')

    except ValueError:
        print('Please enter a number')
        continue
