# Exceptions (so, the program will never crash)
try:
    age = int(input('Enter the number: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero!')
except ValueError:
    print('Invalid value')

# Classes in python
class PointClass:
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

point1 = PointClass() #create new object
point1.draw()  #objects are the instance of class

point1.x = 10
point1.y = 20
print(point1.x)

point2 = PointClass()
point2.x = 66
print(point2.x)

#constructor in classes
class Axis:
    def __init__(self, x, y): #this is a constructore
        self.x = x  #self represents the current object
        self.y = y

aaxis = Axis(10,25)
print(aaxis.x)
aaxis.y = 25
print(aaxis.y)

# Exec 1 - classes
class Person:
    def __init__ (self, name):
        self.name = name
    def talk(self):
        print(f"Hi, im {self.name}")

john = Person("John smith")
john.talk()

bob = Person("Bob polly")
bob.talk()

# Inheritance
class Mammals:
    def walk(self):
        print("walk")

class Dog(Mammals):
    pass   # with pass we can create empty class without error

class Cat(Mammals):
    def meow(self):
        print("Meow")

dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.meow()


# Import modules

#File1 name - converters.py (Module)
def lbs_kg(weight):
    return weight * 0.45

def kb_lbs(weight):
    return weight / 0.45

#File2 name - app.py
import converters

weight11 = converters.lbs_kg(70)
print(weight11)

#File3 name app2.py
from converters import kg_lbs

print(kg_lbs(80))

#Exec 2 - modules

#Filename - utils.py
def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

#Filename - app.py
from utils import find_max

number = [5,10,66,99,10,2]
max1 = find_max()
print(max1) # max is also an inbuilt python function to find max value [ print(max{numbers}) ]
