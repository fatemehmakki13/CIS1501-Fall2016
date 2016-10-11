def setupGradebook():
	gradeBook = {}
	name = input("Please enter a student's name: ")
	while name != "quit":
		gradeBook[name] = 0
		name = input("Please enter a student's name or quit to finish: ")
	return gradeBook

def getCategoryScore( gradeBook, categoryName ):
	for name in gradeBook:
		gradeBook[name] += int(input("Please enter the score for " + name + "'s " + categoryName + ": ") )

def displayMenuAndReturnChoice():
	print("Please select an option:")
	print("\tEnter a student's name to lookup their score")
	print("\tEnter Minimum to get the minimum score for the class")
	print("\tEnter Maximum to get the maximum score for the class")
	print("\tEnter Average to get the average score for the class")
	print("\tEnter Quit to close the gradebook")
	return input()

def getStudentScore( gradeBook, name ):
	if name in gradeBook:
		print("%s's score is:%d" % ( name, gradeBook[name] ) )
	else:
		print("%s was not found in the gradebook!" % name )

def getMinimumScore( gradeBook ):
	print("The minimum score in the class is: %d" % min(gradeBook.values()) )
	min = 100000
	for names in gradeBook:
		if gradeBook[names] < min:
			min = gradeBook[names]
	

def getMaximumScore( gradeBook ):
	print("The maximum score in the class is: %d" % max(gradeBook.values()) )
	
def getAverageScore( gradeBook ):
	print("The average score in the class is: %d" % ( sum(gradeBook.values()) / len( gradeBook ) ) )

gradeBook = setupGradebook()

getCategoryScore(gradeBook, "quiz")
getCategoryScore(gradeBook, "lab")
getCategoryScore(gradeBook, "midterm")
getCategoryScore(gradeBook, "final")
getCategoryScore(gradeBook, "project")
getCategoryScore(gradeBook, "Zbook")

choice = displayMenuAndReturnChoice()
while ( choice != "Quit" ):
	if choice == 'Minimum':
		getMinimumScore(gradeBook)
	elif choice == 'Maximum':	
		getMaximumScore(gradeBook)
	elif choice == 'Average':
		getAverageScore(gradeBook)
	else:
		getStudentScore( gradeBook, choice )
	choice = displayMenuAndReturnChoice()
