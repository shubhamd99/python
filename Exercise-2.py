# While Loop
i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done...") # 1 2 3 4 5 Done...

i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done...") # * ** *** **** ***** Done...

#Exec 1 Guess Game with 3 guess limit
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print("Maximum numbers of guesses exceeds")

#Exec 2 Car Game
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped...")

    elif command == "status":
        if started:
            print("Car is running at full speed")
        else:
            print("Car is not running")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
status - to check the status of the car
quit - to exit the game
""")
    elif command == "quit":
        break;
    else:
        print("Sorry, i don't understand the command")
    

# For Loop (iterate through the statment provided)
for item in 'Python':
    print(item) # P y t h o n

for item in ['Josh', 'Smith', 'Rajesh']:
    print(item) # It prints each items in a row

for item in range(10):
    print(item) # 0 to 9

for item in range(5, 10):
    print(item) # 5 to 9


for item in range(5, 10, 2):
    print(item) # 5, 7, 9

price_chart = [20,30,50,60]

total = 0
for price in price_chart:
    total += price

print(f"the total price is {total}")

# Nested Loop (one loop inside another loop)
for x in range(4):
    for y in range(3):
        print(f"({x},{y})") # (0,0) (0,1) (0,2) (1,0)...


numbers = [5,2,5,2,2]

#my way
for x_count in range(1):
    for y_count in numbers:
        print('*' * y_count)

# Another way withou nesting is'
for x in numbers:
    print('*' * x)
        
#nested loop way
for xx_count in numbers:
    output = ''
    for count in range(xx_count):
        output += 'x'
    print(output)

# Lists in python
names = ['josh', 'madam', 'vanish', 'vandita', 'shubham']
print(names)
print(names[0]) #josh
print(names[-2]) #vandita
print(names[2:]) #['vanish', 'vandita', 'shubham']
print(names[2:4]) #['vanish', 'vandita']

names[0] = 'Robin' # remove john with robin
print(names)

#Exec 3 (Largest number)
numbers = [10,20,5,60,72,92,101,22]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)


# 2D list (Where each item in the list is in another list. Matrix)
matrix = [
    [1,2,3,4],
    [5,8,10,90],
    [20,6,11,22]
]

print(matrix[0][1]) #2

matrix[0][1] = 23
print(matrix[0][1]) #23

for row in matrix:
    for item in row:
        print(item) #prinst all items in the list


# List Methods

numbers = [5,2,7,5,4,6]

numbers.append(13) # adds to the ned of list
numbers.insert(0, 10) #inserts 10 at the beginning
numbers.remove(7)
print(numbers)

print(50 in numbers) #check the presence of number in the list (True or False)
print(numbers.count(5)) # 2 because there is two 5

numbers.sort()
numbers.reverse()
print(numbers) # sorting the list

numbers2 = numbers.copy() # copy the list, create a clone

numbers.clear() #clear the list
numbers.pop() #last item is removed
numbers.index(5) #returns the index of 5

# Exec 4 - Remove the duplicates
numbers = [2,6,5,6,7,252,52,52,6,9,2]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)


