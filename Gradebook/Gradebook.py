gradebook = {
	'Matt' : 0,
	'Robert' : 0,
	'Susan' : 0,
	'Bryant' : 0, 
	'Fatemeh' : 0,
}

# Labs grade
gradebook['Matt'] += int ( input("Please enter Matt's lab points:"))
gradebook['Robert'] += int ( input("Please enter Robert's lab points:"))
gradebook['Susan'] += int ( input("Please enter Susan's lab points:"))
gradebook['Bryant'] += int ( input("Please enter Bryant's lab points:"))
gradebook['Fatemeh'] += int ( input("Please enter Fatemeh's lab points:"))

# Midterm grade
gradebook['Matt'] += int ( input("Please enter Matt's midterm points:"))
gradebook['Robert'] += int ( input("Please enter Robert's midterm points:"))
gradebook['Susan'] += int ( input("Please enter Susan's midterm points:"))
gradebook['Bryant'] += int ( input("Please enter Bryant's midterm points:"))
gradebook['Fatemeh'] += int ( input("Please enter Fatemeh's midterm points:"))

# Final Exam grade
gradebook['Matt'] += int ( input("Please enter Matt's final exam points:"))
gradebook['Robert'] += int ( input("Please enter Robert's final exam points:"))
gradebook['Susan'] += int ( input("Please enter Susan's final exam points:"))
gradebook['Bryant'] += int ( input("Please enter Bryant's final exam points:"))
gradebook['Fatemeh'] += int ( input("Please enter Fatemeh's final exam points:"))


# Quiz grade
gradebook['Matt'] += int ( input("Please enter Matt's quiz points:"))
gradebook['Robert'] += int ( input("Please enter Robert's quiz points:"))
gradebook['Susan'] += int ( input("Please enter Susan's quiz points:"))
gradebook['Bryant'] += int ( input("Please enter Bryant's quiz points:"))
gradebook['Fatemeh'] += int ( input("Please enter Fatemeh's quiz points:"))

# Project grade
gradebook['Matt'] += int ( input("Please enter Matt's project points:"))
gradebook['Robert'] += int ( input("Please enter Robert's project points:"))
gradebook['Susan'] += int ( input("Please enter Susan's project points:"))
gradebook['Bryant'] += int ( input("Please enter Bryant's project points:"))
gradebook['Fatemeh'] += int ( input("Please enter Fatemeh's project points:"))

# Zybook grade
gradebook['Matt'] += int ( input("Please enter Matt's zybook points:"))
gradebook['Robert'] += int ( input("Please enter Robert's zybook points:"))
gradebook['Susan'] += int ( input("Please enter Susan's zybook points:"))
gradebook['Bryant'] += int ( input("Please enter Bryant's zybook points:"))
gradebook['Fatemeh'] += int ( input("Please enter Fatemeh's zybook points:"))

print( "Matt's final grade: ", gradebook['Matt'] )
print( "Robert's final grade: ", gradebook['Robert'] )
print( "Susan's final grade: ", gradebook['Susan'] )
print( "Bryant's final grade: ", gradebook['Bryant'] )
print( "Fatemeh's final grade: ", gradebook['Fatemeh'] )

print( 'Total points:', sum( gradebook.values() ) )
print( 'Average points: ', sum( gradebook.values() )/len(gradebook) )
print( 'Max points: ', max( gradebook.values() ) )
print( 'Min points: ', min( gradebook.values() ) )

grades = {'A': 90, 'B': 80, 'C': 70}

if ( gradebook['Matt'] >= grades['A'] ):
	print ( "Matt got an A!")
elif ( gradebook['Matt'] >= grades['B'] ):
	print ( "Matt got an B!")
elif ( gradebook['Matt'] >= grades['C'] ):
	print ( "Matt got an C!")
else:
	print ( "Matt failed!")

if ( gradebook['Robert'] >= grades['A'] ):
	print ( "Robert got an A!")
elif ( gradebook['Robert'] >= grades['B'] ):
	print ( "Robert got an B!")
elif ( gradebook['Robert'] >= grades['C'] ):
	print ( "Robert got an C!")
else:
	print ( "Robert failed!")