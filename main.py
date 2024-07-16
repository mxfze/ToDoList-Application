import os
import time
from logo import art
import json

command = "cls"
database= "db.txt"

with open(database, "r") as f:
    lines = f.read()

print(lines)
data = json.loads(lines)


def menu():
    os.system(command)
    print(f"{art}\n")
    choice = int(input("================================\nWhat would you like to do?\n================================\n[1] View a To Do List\n[2] Edit one of your To Do Lists\n[3] Create / Delete a To Do List\n================================\n-> "))
    if choice == 1:
        view()
    elif choice == 2:
        edit()

def edit():
    msg = "Would you like to add [A] or remove [R] something?"
    msg2 = "Input what you would like to add to this list:"
    os.system(command)

    print("Select a list to edit:\n[B] -> Go Back\n======================")
    for v, i in enumerate(data):
        print(f"[{v+1}] {i["Name"]}")
        print("======================")
        edit_choice = input("-> ")

        if edit_choice.upper() =="B":
            menu()

        elif int(edit_choice) <= len(data) and int(edit_choice) != 0:
            edit_choice = int(edit_choice)
            list_to_edit = data[edit_choice - 1]
            

            os.system(command)
            print(f"Selected list: {list_to_edit["Name"]}\n{msg}\n{"=" * len(msg)}")

            add_or_remove = input("-> ")
            if add_or_remove.upper() == "A":
                os.system(command)
                print(f"Selected list: {list_to_edit["Name"]}\n{msg2}\n{"=" * len(msg2)}")
                addition = input("-> ")
                last_item = list(list_to_edit.items())[-1]
                print(last_item)
                placeholder = int(last_item[0]) + 1
                print(placeholder)
                index_to_add = str(placeholder)
                list_to_edit[index_to_add] = addition
                print(f"You have succesfully added {addition} to your list.")
                time.sleep(2)
                menu()



def view():
    option = ""
    length = len(data)
    os.system(command)
    print("Select a list to view:\n[B] -> Go Back\n======================")
    for v, i in enumerate(data):
        print(f"[{v+1}] {i["Name"]}")
    print("======================")
    try:
        option = input("-> ")
    except ValueError:
        print("Invalid Option")
        time.sleep(2)
        view()
    if option.upper() =="B":
        menu()
    if option == "":
        print("Invalid Option")
        time.sleep(2)
        view()
    elif int(option) <= len(data) and int(option) != 0:
        option = int(option)
        selected = data[option-1]
        os.system(command)
        for x in selected:
            print(f"{x}: {selected[x]}")
        print("======================")
        option = input("[Any key to go back] ")
        if len(option) >= 0:
            view()

    else:
        print("Invalid Option")
        time.sleep(2)
        view()
    


menu()