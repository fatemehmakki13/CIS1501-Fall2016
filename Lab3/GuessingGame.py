magicNumber = 42

guess = int( input( 'Guess a number 1-100: ' ) )
numberOfGuesses = 1

if guess > magicNumber:
	print('too high!')
elif guess < magicNumber:
	print('too low!')
else:
	print('You guessed it in', numberOfGuesses, 'guess!')
	
if guess != magicNumber:
	numberOfGuesses += 1
	guess = int( input( 'Guess again (1-100): ' ) )
	if guess > magicNumber:
		print('too high!')
	elif guess < magicNumber:
		print('too low!')
	else:
		print('You guessed it in', numberOfGuesses, 'guess!')
		
if guess != magicNumber:
	numberOfGuesses += 1
	guess = int( input( 'Guess again (1-100): ' ) )
	if guess > magicNumber:
		print('too high!')
	elif guess < magicNumber:
		print('too low!')
	else:
		print('You guessed it in', numberOfGuesses, 'guess!')
		
if guess != magicNumber:
	numberOfGuesses += 1
	guess = int( input( 'Guess again (1-100): ' ) )
	if guess > magicNumber:
		print('too high!')
	elif guess < magicNumber:
		print('too low!')
	else:
		print('You guessed it in', numberOfGuesses, 'guess!')

if guess != magicNumber:
	numberOfGuesses += 1
	guess = int( input( 'Guess again (1-100): ' ) )
	if guess > magicNumber:
		print('too high!')
	elif guess < magicNumber:
		print('too low!')
	else:
		print('You guessed it in', numberOfGuesses, 'guess!')