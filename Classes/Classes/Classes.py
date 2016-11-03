class Person:
    Specices = 'Human'

    def __init__(self, name, heightInInches, eyeColor):
        """
        name: Name. String
        heightInInches: height in inches. Int
        eyeColor: Eye Color. String
        """
        self.Name = name
        self.Height = heightInInches
        self.EyeColor = eyeColor

    def Jump(self):
        print(self.Name + " jumped!")

    def __str__(self):
        return self.Name + "\n" + self.EyeColor + "\n" + (str)(self.Height // 12) + "' " + (str)(self.Height % 12) + '"'

    def __lt__(self, other):
        if self.Height < other.Height:
            return True
        else:
            return False

    def __eq__(self, other):
        return self.Name == other.Name and self.EyeColor == other.EyeColor and self.Height == other.Height


def MakePersonJump(p):
    p.Jump()

class_list = []
eric = Person(name='Eric', eyeColor='Hazel', heightInInches=74 )
class_list.append( eric )
class_list.append( Person('Bryant', 70, 'Hazel' ) )
class_list.append( Person('Bryant', 70, 'Hazel' ) )

for person in class_list:
    print(person)
    MakePersonJump(person)

if class_list[0] < class_list[1]:
    print( class_list[0].Name + " is shorter than " +  class_list[1].Name )
else:
    print( class_list[0].Name + " is taller than " +  class_list[1].Name )

if class_list[1] == class_list[2]:
    print("same person!")