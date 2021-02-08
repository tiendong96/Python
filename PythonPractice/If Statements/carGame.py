command = ""
started = False
while True:
    command = input("> ").lower()
    if command == 'help':
        print(""" 
start - to start the car
stop - to stop the car
quit - to exit the game
        """)
    elif command == 'start':
        if started:
            print(f'The car is already started!')
        else:
            started = True
            print(f'The car is started!')

    elif command == 'stop':
        if not started:
            print(f'The car is already stopped!')
        else:
            started = False
            print(f'The car is stopped')
    elif command == 'quit':
        break
else:
    print("Sorry, that command does not exist")
