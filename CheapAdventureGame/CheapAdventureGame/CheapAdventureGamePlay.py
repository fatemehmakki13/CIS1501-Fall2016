import os

command = input("Welcome to the Cheap Adventure Game - What do you want to do ( type HELP for a list of commands )? ")
while command != 'asdf':
    if command == 'HELP':
        for dirname, subdirs, files in os.walk('.'):
            for file in files:
                if str(file).endswith('.game'):
                    print(str(file).replace('.game',''))
        command = input("What do you want to do? ")
    else:
        command += ".game"
        if os.path.exists(command):
            file = open(command)
            print(file.read())
            file.close()
            command = input("What do you want to do? ")
        else:
            command = input("That is not a valid command. What do you want to do? ")