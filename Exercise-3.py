#Tuples (they are immutable, we cannot change their propeties)
numbers = (1,2,3)
print(numbers[0])

#unpacking
coordinates = (1,2,3)
x, y, z = coordinates #it assigns the x with coordinates[0], y with ... (short hand)
print(y)

coordinates = [1,2,3]
x, y, z = coordinates 
print(z)

# Dictionaries (here we can store key-value pairs, keys should be unique like it not accepts two age:)
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

customer["name"] = "Shubham Dhage"

print(customer["age"])
print(customer.get("name"))
print(customer.get("birthday", "April 4, 1997"))

# Exec 1 - numbers to string
phone = input("Phone no. : ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "Only supports upto 4") + " "
print(output)

# Exec 2 - string to Smiley
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "(Smile)",
    ":(": "(Sad)"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

# Functions 
def greet_user(first_name, last_name): #positional arguments, both are required to run function
    print(f"Hello, {first_name} {last_name}")
    print("How r u?")


greet_user("Marry","Goli")
greet_user("Shubham","Dhage")
# first parameter should be positional and second may be keyword arguments
greet_user(last_name="Shubham",first_name="Dhage") #keyword arguments (it imporves readability)


