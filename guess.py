# This is a Guess the number game.
import random

GuessesTaken = 0
highlimit = 30
print('Hello! what is your name?')
myName =  input()

number = random.randint(1, highlimit)
print('well, ' + myName + ', I am  thinking of a number between 1 and '+ str(highlimit) + '.')

for guessesTaken in range(6):
    print('Take a guess')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is to low.')

    if guess > number:
        print('Your guess is to high')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('good job, ' + myName + '! you guessed my number in ' +    guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')