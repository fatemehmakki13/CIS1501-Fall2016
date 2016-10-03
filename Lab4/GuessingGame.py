import random

playAgain = 'yes'

while playAgain[0].lower() == 'y':
	maxNumberToGuess = int( input( "How high of a number would you like to guess to? "))
	randomNumber = random.randint(1, maxNumberToGuess )
	guess = int( input( 'Guess a number 1-%d: ' % maxNumberToGuess ) )
	numberOfGuesses = 1

	while guess != randomNumber:
		if guess > randomNumber:
			print('too high!', end=' ')
		elif guess < randomNumber:
			print('too low!', end='  ')
			
		guess = int( input( 'Guess a number 1-%d: ' % maxNumberToGuess ) )
		numberOfGuesses += 1
		
	print('You guessed it in %d guesses!' % numberOfGuesses)
	
	playAgain = input("Do you want to play again? ( Yes or No )" )