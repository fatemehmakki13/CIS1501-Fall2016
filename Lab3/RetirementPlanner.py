currentAge = int(input('How old are you? ') )
currentSavings = int(input('How much do you have saved for retirement? ') )
targetRetirementSavings = int(input('How much do you want to have saved for retirement? ' ) )
targetRetirementAge = int(input('At what age would you like to retire? ' ) )
yearlySavings = int( input( 'How much are you saving each year for retirement? ' ) )

projectedSavings = currentSavings + ( targetRetirementAge - currentAge ) * yearlySavings

if projectedSavings > targetRetirementSavings:
	print('At your current rate, you will have $' + projectedSavings, ' by age', targetRetirementAge )
else:
	yearsToReachGoal = ( targetRetirementSavings - currentSavings ) / yearlySavings
	ageAtGoal = currentAge + yearsToReachGoal 
	print('At your current savings rate, you will be', ageAtGoal, 'years old when you hit your target savings' )
	
