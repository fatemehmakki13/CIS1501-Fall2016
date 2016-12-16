import os 

PickDirection = input('Welcome to marvelous adventure. Which direction would you like to go? (type DIRECTION for a list of commands. )')

while PickDirection != 'DustyTheBunny':

    if PickDirection == 'DIRECTION':

        for dirname,subdirs, files in os.walk('.'):

            for file in files:

                if str(file).endswith('.game'):

                    print(str(file).replace('.game',''))

        PickDirection = input("What do you want to do? ")

    else:

        PickDirection += ".game"
        command = '' 
        if os.path.exists(command):
            file = open(command)
            print(file.read())
            file.close()
            PickDirection = input("What do you want to do? ")
        else:
            PickDirection = input("That is not a valid command. What do you want to do? ")
