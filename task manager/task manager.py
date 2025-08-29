import questionary
import getpass
import json
from tabulate import tabulate
import hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login():
    while True:
        choice = questionary.select("choose an option:",
                                choices=[ "login", "register new user","Exit"]).ask()
        if choice == "register new user" :
            username = input("please enetr a username:")
            if username in users_list:
                print("user already exist. please login or use a new username and try again")
            else :
                while True:
                    password = input("please enter a password:")
                    password2 = input("please reenter your password:")
                    if password == password2:
                        hashed_password = hash_password(password)
                        users_list[username] = str(hashed_password)
                        print("Registration successful!")
                        with open ("users_list_save.json","w") as A:
                            json.dump(users_list,A)
                        break
                    else :
                        print("passwords doesn't match please set a new password")
        if choice == "login":
            global username1
            username1 = input("please enter your username:")
            if username1 in users_list:
                password3 = getpass.getpass("please type your password (it will not be shown on screen):")
                hashed_password2 = hash_password(password3)
                if str(hashed_password2) == users_list[username1]:
                    print("login successful")
                    global tasks_list
                
                    try:
                        tasks_list = super_list[username1]
                    except:
                        tasks_list = []
                    
                    tasks()
                else :
                    print("incorrect password.")
            else:
                print("user not found")
        if choice == "Exit":
            with open ("users_list_save.json","w") as A:
                json.dump(users_list,A)
            if username1 is not None:
                super_list[username1] = tasks_list
            else:
                pass
            with open ("super_list_save.json","w") as B:
                json.dump(super_list,B)    
            exit()

def tasks() : 

    while True:
        choice1 = questionary.select("choose an option:", choices = ["add new task","view tasks","edit tasks","Previous menu"]).ask()
        if choice1 == "add new task":
            task1 = input( "please enter your task:")
            description = input("please provide a description for the task :")
            task_entry = {"task": task1, "status": "incomplete", "description" : description}
            tasks_list.append(task_entry)
        
        if choice1 == "edit tasks":
            choice = [ item["task"] for item in tasks_list]
            choice2 = questionary.select("choose an option", choices =choice).ask()
            if choice2 :
               choice3 =  questionary.select("choose an option:",choices=["mark as done","remove task"] ).ask()

               if choice3 == "mark as done":
                    for item in tasks_list :
                        if item["task"] == choice2:
                            item["status"]="done"
                            break
               if choice3 == "remove task":
                for item in tasks_list :
                        if item["task"] == choice2:
                            tasks_list.remove(item)
                            break      
        if choice1 == "view tasks":
            print(tabulate(tasks_list, headers="keys",tablefmt="pretty"))
        
        if choice1 == "Previous menu":
            super_list[username1] = tasks_list
            with open ("super_list_save.json","w") as B:
                json.dump(super_list,B)               
            return
def main():
   
    global users_list,super_list,tasks_list,username1
    users_list = {}
    super_list = {}
    tasks_list = []
    username1 = None   

    try:
        with open ("users_list_save.json","r") as x:
            users_list = json.load(x)
        with open ("super_list_save.json","r") as y:
            super_list = json.load(y)            
    except:
       pass
    login()                   
main()      






        