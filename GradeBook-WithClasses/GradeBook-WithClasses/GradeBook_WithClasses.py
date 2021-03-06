class GradeBook:
    def __init__( self, className, students ):
        self.className = className
        self._students = {}
        self.categoriesAndMaxScore = {}
        for student in students:
            self._students[student] = {}

    def AddCategory( self, category, maxScore ):
        if self.GetSumOfCategoriesMaxScore() + maxScore > 100:
            raise ValueError('Sum of max scores is above 100. Current sum is: ' + str(self.GetSumOfCategoriesMaxScore()) )
        for scores in self._students.values():
            scores[category] = 0
            self.categoriesAndMaxScore[category] = maxScore

    def GetAverageGrade( self ):
        totalScore = 0
        for scores in self._students.values():
            totalScore += sum(scores.values())
        averageScore = totalScore / len(self._students)
        return averageScore

    def GetCategories( self ):
        return self.categoriesAndMaxScore.items()
    
    def GetSumOfCategoriesMaxScore( self ):
        return sum(self.categoriesAndMaxScore.values() )

    def GetScoreForCategoryForStudent( self, student, category ):
        '''Returns student's score for category or -1 if not found'''
        return self._students.get(student, {} ).get(category, -1)

    def GetTotalGradeForStudent( self, student ):
        '''Returns student's letter grade or Not Found'''
        if student in self._students:
            totalScore = sum( self._students[student].values() )
            if totalScore >= 94:
                return 'A'
            elif totalScore >= 90:
                return 'A-'
            elif totalScore >= 87:
                return 'B+'
            elif totalScore >= 84:
                return 'B'
            elif totalScore >= 80:
                return 'B-'
            elif totalScore >= 77:
                return 'C+'
            elif totalScore >= 74:
                return 'C'
            elif totalScore >= 70:
                return 'C-'
            elif totalScore >= 67:
                return 'D+'
            elif totalScore >= 64:
                return 'D'
            else:
                return 'F'
        else:
            return 'Not Found'

    def GetStudents( self ):
        students = list( self._students.keys() )
        students.sort()
        return students

    def UpdateScore( self, student, category, score ):
        if student in self._students:
            if category in self._students[student]:
                if score < 0:
                    raise ValueError('Score can not be less than 0')
                if score > self.categoriesAndMaxScore[category]:
                    raise ValueError('Score can not be more than than '+ str(self.categoriesAndMaxScore[category]))
                self._students[student][category] = score

    def __str__( self ):
        output = 'Grades for: ' + self.className + '\n'
        for student, grades in self._students.items():
            output += student + " - Total Grade: " + self.GetTotalGradeForStudent( student ) + "\n"
            for category, score in grades.items():
                output += "\t" + category + ": " + str(score) + "\n"
            output += '\n'
        output += '\n'
        return output

def PrintMenu():
    print("Pick and option:")
    print("e - Enter a class name")
    print("a - Display class average scores")
    print("p - print class grade books" )
    print('q - Quit')
    return input("Enter a choice: ")

gradeBooks = []
className = input("Enter a class name or DONE to stop entering classes: ")
while className != 'DONE': 
    students = []
    name = input("Enter a student name or DONE to stop entering names: ")
    while name != 'DONE':
        students.append( name )
        name = input("Enter a student name or DONE to stop entering names: ")

    classGradeBook = GradeBook( className, students )
    gradeBooks.append(classGradeBook)

    
    while classGradeBook.GetSumOfCategoriesMaxScore() != 100:
        category = input("Enter a grade category: ")
        maxScore = -1
        while maxScore < 0 or maxScore + classGradeBook.GetSumOfCategoriesMaxScore() > 100:
            try:
                value = input("Enter the max score for " + category + ": ")
                maxScore = int(value)
                classGradeBook.AddCategory(category, maxScore)
                break
            except ValueError as exception:
                print(exception)

    for student in classGradeBook.GetStudents():
        for category, max in classGradeBook.GetCategories():
            score = -1
            while score < 0 or score > max:
                try:
                    value = input("Please enter the score for " + student + "'s " + category + ": ")
                    score = float(value)
                    classGradeBook.UpdateScore( student, category, score )
                except ValueError as exception:
                    print(exception, "- Please enter a value between 0 and", max )

    className = input("Enter a class name or DONE to stop entering classes: ")


choice = PrintMenu()
while choice != 'q':
    if choice == "a":
        for classs in gradeBooks:
            print("Average score for: ", classs.className, "-", classs.GetAverageGrade() )
    elif choice == 'e':
        className = input("enter the class name")
        for gradeBook in gradeBooks:
            if gradeBook.className == className:
                print("Enter a choice: ")
                print("s - Get student grade")
                print("ls - List students")
                print('lc - list categories')
                choice = input()
                if choice == 's':
                    studentName = input("enter the student name")
                    print( gradeBook.GetTotalGradeForStudent(studentName) )
                elif choice == 'ls':
                    for student in gradeBook.GetStudents():
                        print(student)
                elif choice == 'lc':
                    for category in gradeBook.GetCategories():
                        print(category)
    elif choice == 'p':
        for gradeBook in gradeBooks:
            print(gradeBook)
            print()

    choice = PrintMenu()