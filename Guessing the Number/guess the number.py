# generate a random number
# if the number user inputs is greater than generated random number print too high
# if the number user inputs is less than generated random number print too low
# if the number user inputs is  equal to the generated random number print congratulations you guessed the correct number {number}

import random


random_number = random.randint(1,100)

while True:
    user_number = int(input("GUESS D NUMBER between 1 & 100: "))
    if user_number == random_number:
        print(f"congratulations you guessed the correct number {random_number}")
        break
    elif user_number > random_number:
        print(f"{user_number} TOO HIGH!")
    elif user_number < random_number:
        print(f"{user_number} TOO LOW!")
    else:
        print(f"{user_number} INVALID!")

        