import os
import time
import json

command = "cls"
database= "db.txt"

with open(database, "r") as f:
    lines = f.read()

data = json.loads(lines)


def menu():
    #os.system(command)
    option = input("What would you like to do?\n===============================\n[1] View a ToDo List\n[2] Edit one of your ToDo Lists\n[3] Create / Delete a ToDo List\n===============================\n-> ")

