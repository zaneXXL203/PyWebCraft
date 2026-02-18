import random

emojis = {
    "R": "🪨",
    "P": "📃",
    "S": "✂️",
}

def game():
    while True:
        user_choice = input("R | P | S | Q: ").strip().upper()
        if user_choice == "Q":
            print("Thanks for Playing")
            break
        elif user_choice not in emojis:
            print("INVALID INPUT!")
            continue

        computer_choice = random.choice(list(emojis.keys()))

        print(f"You chose: {emojis[user_choice]}")
        print(f"Computer chose: {emojis[computer_choice]}")

        if user_choice == computer_choice:
            print("TIE! 🪢")
        elif((user_choice == "R" and computer_choice == "S") or
             (user_choice == "S" and computer_choice == "P") or
             (user_choice == "P" and computer_choice == "R")):
            print("YOU WIN! 🏆")
        else:
            print("💻 WINS!")
game()

































# def game():
#     while True:
#         user_choice = input("R | P | S | Q: ").upper()
#
#         if user_choice == "Q":
#             print("Goodbye!")
#             break
#
#         if user_choice not in emojis:
#             print("INVALID choice!")
#             continue
#
#         computer_choice = random.choice(list(emojis.keys()))
#
#         print(f"You chose {emojis[user_choice]}")
#         print(f"Computer chose {emojis[computer_choice]}")
#
#         if user_choice == computer_choice:
#             print("TIE! 🪢")
#         elif
#             print("YOU WIN! 🏆")
#         else:
#             print("COMPUTER WINS! 🏆")
#
# game()

     
            

# get user input
# r = rock p = paper s = scissors
# define r > s, s > p, p > r
# if userinput is r computer will roll a random element 
# if computer element is greater than yours or yours is greater than computers - you win
# then print you picked what you pick or computer picked and won