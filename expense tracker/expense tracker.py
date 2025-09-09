import questionary
from tabulate import tabulate
import json 

try:
    with open ("C:/Users/Vishnu/Desktop/python tests/expenses_list.json","r") as s:
        expenses_list = json.load(s)
except :
    expenses_list=[]

def budget():
    total_budget = input("please enter your monthly budget:")
    total_expense = sum(float(item["amount"])for item in expenses_list)
    if float(total_budget)>float(total_expense):
        balance = float(total_budget)-float(total_expense)
        print("you have not exceeded budget and your remaining credit is",balance)
    else:
        balance = float(total_expense)-float(total_budget)
        print("you have exceeded your budget by", balance)

def expenses():
    while True:
        choice = questionary.select( "Choose an option:",
            choices=[
                "Add Expense",
                "View Expenses",
                "track budget",
                "Exit"
            ]
        ).ask()
        if choice == "Add Expense":
            date = input("please input date in dd-mm-yyyy format:")
            structure = date.split("-")
            if 0 < int(structure[0]) < 32:
                if 0 < int(structure[1]) < 13:
                    category = input("please enter category of expense :")
                    amount = input("please enter the amount spent:")
                    description = input("Please enter a short description for the expense:")  
                    print("your entry has been recorded.")
                    expense_entry = {'date':date,'category':category,'amount':amount,'description':description}
                    expenses_list.append(expense_entry)
                    with open ("C:/Users/Vishnu/Desktop/python tests/expenses_list.json","w") as e :
                        json.dump(expenses_list,e)
                else:
                    print("please enter a valid date")
            else:
                print("please enter a valid date")
        if choice == "View Expenses" :
            print(tabulate(expenses_list,headers="keys",tablefmt="pretty"))
        if choice == "Exit":
            exit()
        if choice == "track budget":
            budget()
expenses() 
    

    




