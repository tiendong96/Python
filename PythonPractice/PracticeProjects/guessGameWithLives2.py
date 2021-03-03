#in the previous iteration this code uses breaks
#however, for practice this iteration is going to call inner methods

import random 

class GuessingGame:
    def guess(self, x, lives):
        random_number = random.randint(1,x)
        guess = 0
        while guess != random_number and lives != 0: #while guess is not the random number 
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess < random_number:
                if lives != 0:
                    lives -= 1
                else:
                    break
                print('Sorry guess again, the number you chose is too low')
                print(lives)

            elif guess > random_number:
                if lives != 0:
                    lives -= 1
                else:
                    break
                print('Sorry guess again, the number you chose is too high')
                print(lives)

        if guess == random_number and lives >= 1:
            self.__win(lives)
        elif guess != random_number and lives == 0:
            self.__lose(x, lives)

    def __lose(self, x, lives):
        print(f'You have lost the game. The correct number was {x}, and you only have {lives} left.')

    def __win(self, lives):
        print(f'Congratulations! You have won the game with {lives} left!')

    

test = GuessingGame()
test.guess(10, 4)

