import json

file_name = "to-do list.json"



def load_task():
    try:
        with open(file_name, "r")  as file:
            return json.load(file)
    except:
       return {"tasks": []}


def save_task(tasks):
    try:
        with open(file_name, "w")  as file:
            json.dump(tasks, file)
    except:
       print("Failed to Save.")


def view_task(tasks):
    print()
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No task to Display")
    else:
        print("Your to-do list: ")
        for idx, task in enumerate(task_list):
            status = "[completed]" if task["complete"] else "[pending...]"
            print(f"{idx + 1}. {task['description']} | {status}")


def create_task(tasks):
    description = input("enter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_task(tasks)
        print("task added.")
    else:
        print("Description can't be Empty!")


def mark_task_complete(tasks):
    view_task(tasks)
    try:
        task_number = int(input("Enter the task number to mark as Complete: ").strip())
        if 1 <= task_number <= len(tasks):
            tasks["tasks"] [task_number - 1]["complete"] = True
            save_task(tasks)
            print("Task Marked as Complete.")
        else:
            print("Invalid task number!")
    except:
        print("Enter a Valid Task Number.")

def main():
    tasks = load_task()

    while True:
        print("\n To-Do List Manager" )
        print("1. View task")
        print("2. Add task")
        print("3. Complete task")
        print("4. Exit")

        choice = input("Enter your Choice: ").strip()

        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("GoodBye")
            break
        else:
            print("Invalid Input!. Try Again!")


main()