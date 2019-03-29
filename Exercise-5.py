#Generate random values
import random

for i in range(3):
    print(random.random())

for i in range(2):
    print(random.randint(10,20))

#Random pick in a list
members = ['John', 'shubham', 'Robin', 'Pratekk']
leader = random.choice(members)
print(leader)

#Random dice
class Dice:
    def roll(self):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        return dice1,dice2 #return in Tupples, we dont need to add ( brackets ) for returning in tupples


dice = Dice()
print(dice.roll())


#Path Library Python
from pathlib import Path

# Absolute path - root from the harddisk
path = Path("ecommerce")
print(path.exists())

# path.mkdir() - create directory
# path.rmdir() - delete directory

path = Path()
print(path.glob('*')) #search all file in a current path
print(path.glob('*.xls'))
print(path.glob('*.ai'))

for file in path.glob('*.py'):
    print(file)

# Python 3: Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987


