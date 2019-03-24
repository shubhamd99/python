## Python is case sensitive

# Print in console
print('Hello World')
print("shubham's world")

# Taking Input
name1 = input('Tell me your name? ')
print(name1)

# string to integer or float conversion
pounds = input("weight in lbs? ")
kilo = float(pounds) / 2.2
kilo2 = int(pounds) / 2.2
print(kilo)
print(kilo2)

# multiple line strings
multiple_string = '''
hello
how r u
tell me something
'''
print(multiple_string)

# starting and ending index in a string
string1 = 'hello im shubham dhage'
print(string1[0:5]) # Output - hello
print(string1[-5]) # Output - d

# Copying a string
print(string1[:])

# Strings
first_name1 = 'Shubham'
last_name1 = 'Dhage'
message1 = 'Hi, ' + first_name1 + last_name1
message2 = f'Hey, {first_name1} {last_name1} is a coder' #Easy Way
print(message2)


# Length
course = 'Python for beginners'
print(len(course)) # 20

course.upper()

# Methods 
print(course.upper())
print(course.lower())
print(course.title()) # Python for beginners

print(course.find('o')) #4 index
print(course.find('O')) #-1 index

course.replace('beginners', 'professionals') # it replace's the word

print('beginners' in course) #True, because the word is present in the course

# Arthematic operation
print(10 / 3) # 3.3333333333333335
print(10 // 3) # 3
print(10 ** 3) # 10 power 3 = 1000

x = 10
x += 3 #x = x + 3
print(x) #13

y = (10+3) * 2 ** 2
print(y) # 52

x = 2.9
print(round(x)) #3

x = -2.3
print(abs(x)) #2.3 Always return positive (Absolute)

#importing modules (Reusable codes)
import math

print(math.ceil(2.9)) #3
print(math.floor(2.9)) #2

# If Else statement
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print('drink plenty of water')
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")


price_house = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price_house
else:
    down_payment = 0.3 * price_house

print(f"Down payment: ${down_payment}")


# Logical Operators
has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible")

if has_high_income or has_good_credit:
    print("Eligible for loan")

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record: # converts True to false
    print("eligible for loan") 

# Comparison Operators
temperature_day = 30

if temperature_day > 30: # >= <= == !=
    print("It's a hot day")
else:
    print("It's a good day")

name_length = 'shubhamhhh'

if len(name_length) < 3:
    print("Name is too short")
elif len(name_length) > 50:
    print("Name is very long")
elif len(name_length) == 10:
    print("perfect name")
else:
    print("good name")


# Exc 1
import math

enter_weight = int(input('Enter your weight: '))
lbs_kg = input('(lbs) or (kg): ')

if lbs_kg.lower() == 'lbs' or 'L':
    convertion = enter_weight * 0.45
    print(math.ceil(convertion))
elif lbs_kg.lower() == 'kg' or 'K':
    convertion = enter_weight // 0.45
    print(math.ceil(convertion))
else:
    print("Enter only 'lbs' or 'kg' to see results")
