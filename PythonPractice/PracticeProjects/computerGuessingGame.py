#this is essentially the same as the other guessing game, however this will be giving the computers POV
#problem with these guessing games is handling other letter inputs
#One though I have is creating a list with the letters allowed

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

    def __lose(self, x):
        print(f'I have lost the game. The correct number was {x}.')

    def __win(self, x):
        print(f'I won the game! Your number was {x}! How easy!')

    def computer_guess(self, x):
        print(f"Hello, I am a computer and I will try to guess your number. Think of a number between {x}.")
        game_win = False
        random_computer_guess = random.randint(1, x)
        response = input(f"Is the number {random_computer_guess}? [y]es [n]o: ")
        if response.lower() == 'y':
            self.__win(random_computer_guess)
        elif response.lower() == 'n':
            while game_win == False:
                response = input("Is the number [h]igher or [l]ower?: ")
                if response.lower() == 'h':
                    random_computer_guess += 1
                    response = input(f'Is your number {random_computer_guess}? [y]es [n]o: ')
                    if response.lower() == 'y':
                        game_win = True
                elif response.lower() == 'l':
                    random_computer_guess -= 1
                    response = input(f'Is your number {random_computer_guess}? [y]es [n]o: ')
                    if response.lower() == 'y':
                        game_win = True

            if game_win == True:
                self.__win(random_computer_guess)


test = GuessingGame()
#test.guess(10, 4)
test.computer_guess(10)

