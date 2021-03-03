#this game is like the guessing game but the player is now given tries (lives), if the player
#does not figure out the correct number the game will end

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
            print(f'Congratulations! The correct number was {random_number}')
        elif guess != random_number and lives == 0:
            print(f"You lost! You have {lives} lives.")
    

test = GuessingGame()
test.guess(10, 4)
