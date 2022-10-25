#MASTER PASSWORD IS "CLASSICISAAC"
import csv
import re

def main():
    login()
    print("'add' to add new password\n'view' to view existing passwords\n") 
    ask_operation=input("Would you like to add a new password or view existing passwords? ").lower().strip()
    backend(ask_operation)
    print("Your information is secure. Have a great day 🙂")

def add_password():
    #write new details into the csv file
    name=input("Enter App name or Web URL: ").strip().capitalize()
    password=input("Password: ").strip()
    with open("passwords.csv", "a") as file:
        writer =csv.writer(file)
        writer.writerow([name , password])

def view_password():
    #Check if app or url exists in csv file using regular expression 
    ask=input("Which password do you want to view? ").capitalize().strip() 
    text_found=False
    with open("passwords.csv") as file:
        for line in file:
            if re.search(rf"{ask}", line):
                text_found=True
        if not text_found:
            print(f"{ask} password does not exist")
#if app or url exists, print password
    if text_found:
        with open("passwords.csv") as file:
            for row in file:
                row=row.strip()
                row=re.split(r"\W+", row)
                if row[0]==ask:
                    print(f"{ask} Password: {row[1]}")

#Log in with master password
def login():
    tryyy=3
    while True:
        master_pass=input("Enter Master Password: ")
        if master_pass=="CLASSICISAAC":
            break
        else:
            tryyy-=1
            print(f"Invalid Password. You have only try {tryyy} more times")
            if tryyy==0:
                quit()

#select operation you want to carry out
def backend(ask_operation):
    while ask_operation!="quit".lower():
        if ask_operation=="add":
            add_password()
        elif ask_operation=="view":
            view_password()
        else: 
            print("Invalid command\n")
            print("'add' to add new password\n'view' to view existing passwords\n")
            ask_operation=input("Would you like to add a new password or view existing passwords? ").lower().strip()
            continue
        mode=input("Do you want to perform another operation? ").lower()
        if mode=="yes":
            ask_operation=input("Would you like to add a new password or view existing passwords? ").lower().strip()
            continue
        elif mode=="no":
            break
        else:
            print("Invalid command")
            print("'add' to add new password\n'view' to view existing passwords\n") 
            ask_operation=input("Would you like to add a new password or view existing passwords? ").lower().strip()
            continue

if __name__=="__main__":
    main()