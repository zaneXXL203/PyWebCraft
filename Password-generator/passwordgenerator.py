import random
import string



def password_generator():
    length = int(input("ENTER PASSWORD LENGTH: "))
    Uppercase = input("UPPERCASE(yes/no): ")
    SpecialCharacters = input("SpecialCharacters(yes/no): ")
    Digits = input("Digit(yes/no): ")

    if length < 4:
        print("Character needs to be at least 4 characters")
        return

    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if Uppercase == "yes" else ""
    special = string.punctuation if SpecialCharacters == "yes" else ""
    digit = string.digits if Digits == "yes" else ""

    All_Characters = lower + uppercase + special + digit

    required_characters = []
    if Uppercase == "yes":
        required_characters.append(random.choice(uppercase))
    if SpecialCharacters == "yes":
        required_characters.append(random.choice(special))
    if Digits == "yes":
        required_characters.append(random.choice(digit))

    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range(remaining_length):
        characters = random.choice(All_Characters)
        password.append(characters)


    random.shuffle(password)
    str_password = "".join(password)
    return str_password


password = password_generator()
print(password)