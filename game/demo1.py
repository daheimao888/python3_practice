import random

guessesToken = 0
print("Hello! What is your name?")
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20')

while guessesToken < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    guessesToken = guessesToken + 1
    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is to high.')

    if guess == number:
        break

if guess == number:
    guessesToken = str(guessesToken)
    print('Good job,' + myName + '! You guessed my number in ' + guessesToken + ' guesses')
else:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
