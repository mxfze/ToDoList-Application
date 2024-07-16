import os
import time
command = "cls"
database= "db.txt"
def menu():
    os.system(command)
    option = input("What would you like to do?\n===============================\n[1] View a ToDo List\n[2] Edit one of your ToDo Lists\n[3] Create / Delete a ToDo List\n===============================\n-> ")

menu()