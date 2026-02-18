


Create_file = input("Create a TXT file: ")
default = "default.txt"


if Create_file == "":
    with open(default, "w"):
        print(f"Created a {default} File")
elif Create_file:
    with open(Create_file, "w"):
        print(f"Created {Create_file}")

enter_your_message = input("Message: ")

if Create_file:
    with open(Create_file, "a") as your_file:
        your_file.write(enter_your_message)
        print("Message added!")
elif default:
    with open(default, "a") as mandate:
        mandate.write(enter_your_message)
        print("Message added!")