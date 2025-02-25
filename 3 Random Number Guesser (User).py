import random

def computer_guess(x):
    low = 1 
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high because low = high#
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1 
        if feedback == 'l':
            low = guess + 1
    print('Yay! The computer guessed your number, {guess}, correctly!')

computer_guess(10)


#what is a feedback variable and why is it set to an empty string#