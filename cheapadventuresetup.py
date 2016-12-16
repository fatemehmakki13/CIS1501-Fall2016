
command = input("please enter a command/direction a player can do in the game: ")
while command != 'ALLDONE':
    file = open(command+".game", "w")
    file.write(input("Enter a description of that command/direction for the player: "))
    file.close()
    command = input("please enter a command/direction a player can do in the game or ALLDONE to finish the game setup: ")
