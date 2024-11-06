import random

#list of characters
min_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
mays_characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K","L", "M", "N", "O", "P", "Q", "R", "S", "T", "U","V", "W", "X", "Y", "Z"]
all_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K","L", "M", "N", "O", "P", "Q", "R", "S", "T", "U","V", "W", "X", "Y", "Z"]
especial_characters = ["!", "<", ">","=", "?", "¿", "+","-", "_", "/", "$", "%", "@", "#", "*"]
all_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K","L", "M", "N", "O", "P", "Q", "R", "S", "T", "U","V", "W", "X", "Y", "Z", "!", "<", ">","=", "?", "¿", "+","-", "_", "/", "$", "%", "@", "#", "*"]

print("\n")
print("░█▀█░█▀█░█▀▀░█▀▀░█░█░█▀█░█▀▄░█▀▄░░░█▀▀░█▀▀░█▀█░█▀▀░█▀▄░█▀█░▀█▀░█▀█░█▀▄")
print("░█▀▀░█▀█░▀▀█░▀▀█░█▄█░█░█░█▀▄░█░█░░░█░█░█▀▀░█░█░█▀▀░█▀▄░█▀█░░█░░█░█░█▀▄")
print("░▀░░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀░░░░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀░▀░░▀░░▀▀▀░▀░▀\n\n")


num= int(input('- Length of the password: '))

if num <= 3 or num >= 18:
    print("This numer is not in the range requested.")
    quit()

pass_type = int(input('\n Choose the type of password: \n \n 1 - Only lowercase letters. \n 2 - Only uppercase letters. \n 3 - Uppercase and lowercase letters. \n 4 - Especial characters and all letters.\n \n Write the number: '))

print("\n generating the password...\n")


#creating the password list based on the selected type of characters
password = []


if pass_type == 1:
    for i in range(num):
        x = min_characters[random.randint(0, len(min_characters) - 1)]
        password.append(x)

elif pass_type == 2:
    for i in range(num):
        x = mays_characters[random.randint(0, len(mays_characters) - 1)]
        password.append(x)

elif pass_type == 3:
    for i in range(num):
        x = all_letters[random.randint(0, len(all_letters) - 1)]
        password.append(x)

elif pass_type == 4:
    for i in range(num):
        x = all_characters[random.randint(0, len(all_characters) - 1)]
        password.append(x)


#printing the password together
print("The password is:", ''.join(password))
