favoriteAnimal1 = input('What is your favorite animal? ')
favoriteAnimal2 = input('What is your favorite animal? ')
favoriteAnimal3 = input('What is your favorite animal? ')
favoriteAnimal4 = input('What is your favorite animal? ')
favoriteAnimal5 = input('What is your favorite animal? ')
favoriteAnimal6 = input('What is your favorite animal? ')
favoriteAnimals = {
	favoriteAnimal1 : 0,
	favoriteAnimal2 : 0,
	favoriteAnimal3 : 0,
	favoriteAnimal4 : 0,
	favoriteAnimal5 : 0,
	favoriteAnimal6 : 0
}

favoriteAnimals[favoriteAnimal1] = favoriteAnimals[favoriteAnimal1] + 1
favoriteAnimals[favoriteAnimal2] = favoriteAnimals[favoriteAnimal2] + 1
favoriteAnimals[favoriteAnimal3] = favoriteAnimals[favoriteAnimal3] + 1
favoriteAnimals[favoriteAnimal4] = favoriteAnimals[favoriteAnimal4] + 1
favoriteAnimals[favoriteAnimal5] = favoriteAnimals[favoriteAnimal5] + 1
favoriteAnimals[favoriteAnimal6] = favoriteAnimals[favoriteAnimal6] + 1

print ( favoriteAnimal1, 'is the favoriate animal of', favoriteAnimals[favoriteAnimal1], 'people' )
print ( favoriteAnimal2, 'is the favoriate animal of', favoriteAnimals[favoriteAnimal2], 'people' )
print ( favoriteAnimal3, 'is the favoriate animal of', favoriteAnimals[favoriteAnimal3], 'people' )
print ( favoriteAnimal4, 'is the favoriate animal of', favoriteAnimals[favoriteAnimal4], 'people' )
print ( favoriteAnimal5, 'is the favoriate animal of', favoriteAnimals[favoriteAnimal5], 'people' )
print ( favoriteAnimal6, 'is the favoriate animal of', favoriteAnimals[favoriteAnimal6], 'people' )


