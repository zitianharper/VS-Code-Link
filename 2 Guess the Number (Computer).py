import random

def guess(x):
    guess = 0
    random_number = random.randint(1, x)
    while random_number != guess:
        guess = int(input(f'guess a number between 1, {x}: '))
        if guess < random_number:
            print("too low")
        elif guess > random_number:
            print("too high")
    print("congrats, you win")


guess(10)    

git push

