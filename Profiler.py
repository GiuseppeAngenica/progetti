### IMPORT ###

import os
import shutil
import sys
import time
import keyboard
import pyautogui

### BANNER ###
data = {}
os.system("title Profiler")
os.system("color 0a")
print('''
  _____    _____     ____    ______   _____   _        ______   _____  
 |  __ \  |  __ \   / __ \  |  ____| |_   _| | |      |  ____| |  __ \ 
 | |__) | | |__) | | |  | | | |__      | |   | |      | |__    | |__) |
 |  ___/  |  _  /  | |  | | |  __|     | |   | |      |  __|   |  _  / 
 | |      | | \ \  | |__| | | |       _| |_  | |____  | |____  | | \ \ 
 |_|      |_|  \_\  \____/  |_|      |_____| |______| |______| |_|  \_\ ''')
print("\n\n")


### MENU' ###
def menu():
    print("_______________________________________\n")
    print("1. Create a new profile")
    print("2. View the profile summary")
    print("3. Print the profile")
    print("4. Make screenshots")
    print("5. Navigate into database")
    print("6. Add a comment to the Target profile")
    print("0. Exit")
    print("_______________________________________")

    choise = input("\nChoise an option: ")
    if choise == "1":
        os.system("cls")
        newprofile()
    elif choise == "2":
        os.system("cls")
        summary()
    elif choise == "3":
        os.system("cls")
        save()
    elif choise == "4":
        os.system("cls")
        screenshot()
    elif choise == "5":
        os.system("cls")
        database()
    elif choise == "6":
        os.system("cls")
        edit()
    elif choise == "0":
        os.system("cls")
        exitt()

### CREATE A NEW PROFILE ###
def newprofile():
    global data
    data = {"Nome:":input("Nome: "),
    "Cognome:" : input("Cognome: "),
    "Città:" : input("Città di residenza: "),
    "Regione" : input("Regione di residenza: "),
    "Età:" : input("Età: "),
    "Data di nascita:" : input("Data di nascita(es. 26.12.1999): "),
    "Occupazione:" : input("Occupazione: "),
    "Hobbie:" : input("Hobbie: "),
    "Link Instagram:" : input("Link Instagram: "),
    "Link Facebook:" : input("Link Facebook: ")}

    print("\nDONE")
    print("Going to menù...")
    print("\n\n")

    time.sleep(0.5)
    os.system("cls")
    menu()

### PROFILE SUMMARY ###
def summary():
    global data
    print("\n\n")
    print("________________________________________________________\n")
    for x, y in data.items():
        print(x, y)
    print("________________________________________________________\n\n")
    print("Going to menu...")
    print("\n\n")

    time.sleep(0.5)
    input("Press any button> ")
    os.system("cls")
    menu()

### SAVE ###
def save():
    global data
    global x
    global y
    f = open("output.txt", "w")
    for x, y in data.items():
        f.write(x + " " + y + "\n")
    f.close()

    fileig = open('Instagram.bat', 'w')
    fileig.write("start ")
    fileig.write(data["Link Instagram:"])
    fileig.close()

    filefb = open('Facebook.bat', 'w')
    filefb.write("start ")
    filefb.write(data["Link Facebook:"])
    filefb.close()
    
    ###########    FILE MANAGEMENT    ###########
    directorylavoro = os.getcwd()
    destinazione = data["Nome:"] + " " + data["Cognome:"]
    os.makedirs(directorylavoro + "\\" + destinazione)
    shutil.move(directorylavoro + "\\output.txt", directorylavoro + "\\" + destinazione)
    os.makedirs(directorylavoro + "\\" + destinazione + "\\" + "Social Links")
    shutil.move(directorylavoro + "\\Instagram.bat",
    directorylavoro + "\\" + destinazione + "\\Social Links")
    shutil.move(directorylavoro + "\\Facebook.bat", directorylavoro + "\\" + destinazione + "\\Social Links")
    os.rename(directorylavoro + "\\" + destinazione + "\\output.txt", directorylavoro + "\\" + destinazione + "\\" + destinazione + ".txt")
    os.makedirs(directorylavoro + "\\" + destinazione + "\\" + "Screenshot")
    
    print("\n\nDone!\n\n")
    time.sleep(1)
    os.system("cls")
    menu()

### SCREENSHOT ###
def screenshot():
    d = os.getcwd()
    n = 1
    while True:
        try:
            destinazione = input("Target name (type \"close\" to return to the menu): ")
            if destinazione == "close":
                print("Returning to menu...")
                time.sleep(1)
                os.system("cls")
                menu()
            os.chdir(d+"/"+destinazione)
            savepoint = os.getcwd()
        except FileNotFoundError:
            print(f"No file for\"{destinazione}\"")
        else:
            break
    os.system("cls")
    print('''

   _____   _____  _____   ______  ______  _   _ 
  / ____| / ____||  __ \ |  ____||  ____|| \ | |
 | (___  | |     | |__) || |__   | |__   |  \| |
  \___ \ | |     |  _  / |  __|  |  __|  | . ` |
  ____) || |____ | | \ \ | |____ | |____ | |\  |
 |_____/  \_____||_|  \_\|______||______||_| \_|
    ''')
    print("press \"è\" button to take screenshot")
    print("press \"-\" button to return to menu")
    while True:
        if keyboard.is_pressed("è"):
            screenshot = pyautogui.screenshot()
            screenshot.save(savepoint+"/Screenshot/"+str(n)+".png")
            n = n+1
        elif keyboard.is_pressed("-"):
            os.system("cls")
            os.chdir(d)
            menu()

### DATABASE ###
def database():
    print("Digit \"?\" for a list of commands")
    startcwd = os.getcwd()
    
    while 1:
        workin = os.getcwd()
        com = input("\n\n"+workin+"> ")
        if com == "?":
            print('''
 _________________________________\n
 Digit "?" for a list of commands
 Digit "dir" to see the database  
 Digit "cd" to see the Target dir
 Digit ".." to go back dir
 Digit "read" to read Target Info
 Digit "close" to return to menu
 _________________________________''')
        elif com == "dir":
            print("________________________________________\n")
            directory = os.listdir()
            for s in directory:
                print(s)
            print("________________________________________")
        elif com == "cd":
            n = input("Insert Target name> ")
            cwd = os.getcwd()
            os.chdir(cwd + "/" + n)
        elif com == "..":
            os.chdir(startcwd)
        elif com == "read":
            n = input("Insert Target name> ")
            file = open(n+".txt","r")
            print("___________________________________\n")
            print (file.read())
            print("___________________________________")
            file.close()
        elif com == "close":
            os.chdir(startcwd)
            os.system("cls")
            menu()

### EDIT ###
def edit():
    directorylavoro = os.getcwd()
    while True:
        try:
            destinazione = input("Target Name (type \"close\" to return to the menu): ")
            if destinazione == "close":
                print("Returning to menu...")
                time.sleep(1)
                os.system("cls")
                menu()
            else:
                os.chdir(directorylavoro+"/"+destinazione)
            mod = open(destinazione+".txt", "a")
        except FileNotFoundError:
            print(f"Error: No file for \"{destinazione}\"")
        else:
            break
    print(f"Now you're adding a comment into \"{destinazione}\" file.")
    print("Digit \"..\" in a empty string to save and return to the menu")
    print("Digit \"@\" in a empty string to go next line")

    while True:
        text = input("> ")
        if text == "..":
            print("Saving...")
            mod.close()
            print("Returning to the menu...")
            os.chdir(directorylavoro)
            time.sleep(1)
            os.system("cls")
            menu()
        elif text == "@":
            mod.write("\n")
        else:
            mod.write(text)

### EXIT ###
def exitt():
    input("Press any button to exit> ")
    exit()
menu()
