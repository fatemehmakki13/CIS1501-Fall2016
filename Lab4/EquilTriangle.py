# Diamond
#   *
#  ***
# *****
#*******
# *****
#  ***
#   *
#print half rounded down of max spaces - row
#print 1 star

#stars increase by 2
#spaces decrease by 1


maxNumberOfStars = 7
currentNumberOfStars = 1
currentNumberOfSpaces = maxNumberOfStars // 2

while currentNumberOfStars <= maxNumberOfStars:
	for space in range( currentNumberOfSpaces ):
		print(' ', end='')
	for star in range( currentNumberOfStars ):
		print('*', end='')
	print()
	currentNumberOfStars += 2
	currentNumberOfSpaces -= 1

