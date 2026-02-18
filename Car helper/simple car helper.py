# create an input field when users == help lower or upper case 
# print start - start the car, stop - stop the car, quit - to end the program 
# if user something that is not start stop or quit, print i don't understand

user_input = input("CAR! >>> ")
started = False
stopped = False
while True:
    if user_input == "help":
        print("START - start the car.")
        print("STOP - stop the car.")
        print("QUIT - end the program.")
        user_input = input("CAR! >>> ")
    elif user_input == "start":
        if started:
            print("CAR is already started")
        else:
            started = True
            print("STARTING the car...")
        user_input = input("CAR! >>> ")
    elif user_input == "stop":
        if stopped:
            print("CAR is already STOPPED")
        else:
            stopped = True
            print("STOPPED the car...")
        user_input = input("CAR! >>> ")
    elif user_input == "quit":
        print("ENDING program...")
        break   
    elif user_input != "help" and "start" and "stop" or "quit":
        print("I don't understand")
        user_input = input("CAR! >>> ")
    else:
        print("ERROR")
        break