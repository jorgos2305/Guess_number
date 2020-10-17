#Guess number by Jorge T.
#October 2020

import random as rd
import time
import math

#START OF THE PROGRAMM
#Select to numbers to define the range
print("Try to guess the number I'm thinking about...")
print('Thinking of numbers...')
time.sleep(1)
num1 = rd.randint(0, 100)
num2 = rd.randint(0, 100)

#Give th user the range to choose from
if num1 < num2:
    print('Guess a number between {num1} and {num2}'.format(num1=num1, num2=num2))
    low = num1
    high = num2
else:
    print('Guess a number between {num1} and {num2}'.format(num1=num2, num2=num1))
    low = num2
    high = num1

listOfNumbers = list(range(low, high))
computer_choice = rd.choice(listOfNumbers)
#print(computer_choice, 'index:', listOfNumbers.index(computer_choice))

guesses = round(math.log2(len(listOfNumbers))) #chnage for number of possible guesses
while guesses > 0:
    print('You have {guesses} guesses...'.format(guesses=guesses))
    while True:
        try:
            inp = input('Tell me your guess: ')
            user_choice = int(inp)
            if user_choice < 0:
                print('Please, enter only positive integer numbers')
                continue
            break

        except:
            print('You did not enter a number, please try again')
            continue

    if user_choice == computer_choice:
        print("You've done it, you won!")
        break
    elif user_choice < computer_choice:
        print('A little higher...')
    else:
        print('A little lower...')
    guesses -= 1

if guesses == 0:
    print("You lost, better luck next time!")
