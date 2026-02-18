import random


while True:
    dice = input("roll a dice (yes/no): ")
    if dice == "yes":
        dice = random.randint(1, 10)
        print(f"rolled! {dice}")
    elif dice == "no":
        print("thanks for playing!")
        break
    else:
        print("invalid input!")
        
