print("Please enter your name")
userName = input()
print(userName, ", how many credits total do you need to graduate?")
totalCredits = int( input() )
print(userName, ", how many credits have you completed?")
completedCredits = int( input() )
print(userName, ", how many credits do you take per semester")
creditsPerSemester = int( input() )
semesterToGo = ( totalCredits - completedCredits ) / creditsPerSemester
print( userName, ", you have ", semesterToGo, " more semesters until graduation")