import csv
import json



employees = [["name", "age", "job"],
             ["spongebob", 46, "Fry Cook"],
             ["Patrick", 40, "Jobless"],
             ["Sandy", 29, "Scientist"]]

file_input  = input("Enter Your message: " + " ").strip()
file_path = input("Create file in TXT | JSON | CSV or file path: ")
# employees = {
# "manager" : "Mr. Eugene-Krabs",
# "Waiter" : "Squidward-Tentacles",
# "Fry Cook" : "SpongeBoB-squarepants",
# "Nuisance" : "Patrick-Star"
# }

def create():
    if file_input:
        try:
            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                # json.dump(employees, file, indent=4)
                # for employee in employees:
                #     file.write(file_input + ' ')
                #     file.write(employee + "\n")
                for row in employees:
                    writer.writerow(row)
                print(f"The CSV {file_path} was Created!")
        except FileExistsError:
            print(f"The File {file_path} Already Exist!")
    else:
        print("File was Not Created!")

create()