import random 

class GuessingGame:
    def guess(self, x):
        random_number = random.randint(1,x)
        guess = 0
        while guess != random_number:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess < random_number:
                print('Sorry guess again, the number you chose is too low')
            elif guess > random_number:
                print('Sorry guess again, the number you chose is too high')
        print(f'Congratulations! The correct number was {random_number}')

test = GuessingGame()
test.guess(10)
