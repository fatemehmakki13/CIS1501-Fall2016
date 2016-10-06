def printHello():
    print("hello!")

def askForFavoriteFood():
    food = input("What's your favorite food?")
    print(locals())
    return food

printHello()

print(globals())

favoriteFood = askForFavoriteFood()

print(favoriteFood)