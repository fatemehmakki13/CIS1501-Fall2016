# True/False - Correct the false statement
When writing a Python function, you can specify 
what type of parameter should be passed

False - You can not specify the type of parameter to be passed

# True/False - Correct the false statement
A function can return more than value

True

# sample short answer
What can a programmer can use to run the same code multiple times

A - loops, or even functions

# sample short answer
How do you get a users input and ensure that it's a value 1-10

enteredNumber = 0
while not ( enteredNumber <= 10 and enteredNumber >= 1 ):
    enteredNumber = int(input("Enter a number 1-10" ) )


# Sample long answer
# given a collection of ints, return the number of odd ints
# create a function that accepts a collection and counts the odds

def CountOdd( collection ):
    numberOfOddInts = 0
    for number in collection:
        if number % 2 != 0:
            numberOfOddInts += 1
    return numberOfOddInts

someNumbers = ( 1,2,3,4,5,6,7,8,9 )
print ( CountOdd( someNumbers ) )

listOfNumbers = [ -1, -3, -5, -7, -9 ]
print ( CountOdd ( listOfNumbers ) )

dictionaryOfNumbers = { 1 : "One", 2 : "Two", 3 : "Three" }
print ( CountOdd ( dictionaryOfNumbers ) )