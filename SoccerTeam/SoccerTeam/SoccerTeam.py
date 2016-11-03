# Type code here
players = {}
for number in range(1,6):
    jerseyNumber = int(input("Enter player " + str(number) + "'s jersey number: "))
    rating = int(input("Enter player " + str(number) + "'s rating: "))
    players[jerseyNumber] = rating

print()
print()
print("ROSTER")
keys = players.keys()
keysList = list( keys )
keysList.sort()
# keysList = list( players.keys() ).sort()
for key in keysList:
    print("Jersey number: " + str(key) + ", Rating: " + str(players[key]))

choice = ''

while ( choice != 'q' ):
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    print()
    choice = input('Choose an option: ')

    if choice == 'a':
        addPlayer()
    elif choice == 'd':
        removePlayer()
    elif choice == 'u':
        updatePlayer
    elif choice == 'r':
        outputPlayersAboveRating()
    elif choice == 'o':
        outputRoster()