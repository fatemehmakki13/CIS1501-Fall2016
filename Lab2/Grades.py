gradeBook = {
	'Matt' : 0,
	'Robert' : 0,
	'Susan' : 0,
	'Bryant' : 0,
	'Fatemeh' : 0
}

# Labs grade
gradeBook['Matt'] += int( input("Please enter Matt's lab points: ") )
gradeBook['Robert'] += int( input("Please enter Robert's lab points: ") )
gradeBook['Susan'] += int( input("Please enter Susan's lab points: ") )
gradeBook['Bryant'] += int( input("Please enter Bryant's lab points: ") )
gradeBook['Fatemeh'] += int( input("Please enter Fatemeh's lab points: ") )

# Midterm grade
gradeBook['Matt'] += int( input("Please enter Matt's midterm points: ") )
gradeBook['Robert'] += int( input("Please enter Robert's midterm points: ") )
gradeBook['Susan'] += int( input("Please enter Susan's midterm points: ") )
gradeBook['Bryant'] += int( input("Please enter Bryant's midterm points: ") )
gradeBook['Fatemeh'] += int( input("Please enter Fatemeh's midterm points: ") )

# Final Exam grade
gradeBook['Matt'] += int( input("Please enter Matt's Final Exam points: ") )
gradeBook['Robert'] += int( input("Please enter Robert's Final Exam points: ") )
gradeBook['Susan'] += int( input("Please enter Susan's Final Exam points: ") )
gradeBook['Bryant'] += int( input("Please enter Bryant's Final Exam points: ") )
gradeBook['Fatemeh'] += int( input("Please enter Fatemeh's Final Exam points: ") )

# Quiz grade
gradeBook['Matt'] += int( input("Please enter Matt's Quiz points: ") )
gradeBook['Robert'] += int( input("Please enter Robert's Quiz points: ") )
gradeBook['Susan'] += int( input("Please enter Susan's Quiz points: ") )
gradeBook['Bryant'] += int( input("Please enter Bryant's Quiz points: ") )
gradeBook['Fatemeh'] += int( input("Please enter Fatemeh's Quiz points: ") )

# Project grade
gradeBook['Matt'] += int( input("Please enter Matt's project points: ") )
gradeBook['Robert'] += int( input("Please enter Robert's project points: ") )
gradeBook['Susan'] += int( input("Please enter Susan's project points: ") )
gradeBook['Bryant'] += int( input("Please enter Bryant's project points: ") )
gradeBook['Fatemeh'] += int( input("Please enter Fatemeh's project points: ") )

# Zybook grade
gradeBook['Matt'] += int( input("Please enter Matt's zybook points: ") )
gradeBook['Robert'] += int( input("Please enter Robert's zybook points: ") )
gradeBook['Susan'] += int( input("Please enter Susan's zybook points: ") )
gradeBook['Bryant'] += int( input("Please enter Bryant's zybook points: ") )
gradeBook['Fatemeh'] += int( input("Please enter Fatemeh's zybook points: ") )

print( "Matt's final grade: ", gradeBook['Matt'] )
print( "Robert's final grade: ", gradeBook['Robert'] )
print( "Susan's final grade: ", gradeBook['Susan'] )
print( "Bryant's final grade: ", gradeBook['Bryant'] )
print( "Fatemeh's final grade: ", gradeBook['Fatemeh'] )

print( 'Total points: ', sum( gradeBook.values() ) )
print( 'Average points: ', sum( gradeBook.values() ) / len(gradeBook) )
print( 'Max points: ', max( gradeBook.values() ) )
print( 'Min points: ', min( gradeBook.values() ) )