#user has to figure out what the secret number is

winner = 15
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == winner:
        print("You won!")
        break
else: #different from java, if while condition does not pass the else statement will run
    print("You lose!")

