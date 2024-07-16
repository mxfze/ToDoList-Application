import os
import time
import json

command = "cls"
database= "db.txt"

with open(database, "r") as f:
    lines = f.read()

data = json.loads(lines)


def menu():
    os.system(command)
    option = int(input("What would you like to do?\n===============================\n[1] View a To Do List\n[2] Edit one of your To Do Lists\n[3] Create / Delete a To Do List\n===============================\n-> "))
    if option == 1:
        view()


def view():
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
    elif int(option) <= len(data) and int(option) != 0:
        option = int(option)
        os.system(command)
        for i in data[option-1]:
            print(f"{i}: {data[option-1][i]}")
    elif option == "":
        print("Invalid Option")
        time.sleep(2)
        view()
    else:
        print("Invalid Option")
        time.sleep(2)
        view()
    print("======================")
    option = input("[Any key to go back] ")
    if len(option) >= 0:
        view()


menu()