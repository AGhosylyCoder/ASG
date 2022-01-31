# Import all necessary modules
# import random
import colorama  # Make it more colourful!
from colorama import Fore
from pyfiglet import figlet_format

colorama.init(autoreset=True)

import pickle as pick  # For writing, reading files
from datetime import datetime
import os
import operator 


# Setup Variables, Dictionaries or Lists
WeekDayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
Day = datetime.today().weekday()
WeekDay = WeekDayList[Day]
Likeness = 0
ActivitiesList = []
actFilesList = []
ActivitiesDic = {} 
PActivitiesDic = {}
FixedActivitiesDict1 = {"Breakfast": 7} # Morning manditory Activities
FixedActivitiesDict2 = {"Lunch": 12} # After Noon manditory Activities
FixedActivitiesDict3 = {"Dinner": 19} # Night Manditory Activities
FixedActivitiesDict4 = {"Sleep": 21} # When you go to sleep and end your day
devMode = False


# Get all definitions
def hardSave():
    print("Starting Save")
    print("what name do you want to assign to the file")
    _sqna = input()
    pick.dump(ActivitiesList, open(_sqna + ".dat", "wb"))
    actFilesList.append(_sqna + "dat")
    print("Saving Success!")
    softLoad(_sqna)


def hardLoad():
    print("Starting Load")
    print("Which file do you want to load")
    _lqna = input()
    if _lqna not in actFilesList:
        try:
            loaded_activities = pick.load(open(_lqna + ".dat", "rb"))
            print(loaded_activities)
        except FileNotFoundError as e:
            if not devMode:
                error("The File" + _lqna + "not found\n"
                                           "(Make sure that the syntax is correct)")
            else:
                error(e)
        except Exception as e:
            if not devMode:
                error("Something went wrong loading")
            else:
                error(e)


def softLoad(arg1):
    print(pick.load(open(arg1 + ".dat", "rb")))


def new():
    t = 9
    print("Enter activities:(/x to stop registering)")
    _q = None
    while _q != "/x" or t > 24:
        _q = input()
        if _q not in ActivitiesDic and _q != "/x":
            _lq = None
            while type(_lq) is not int:
                try:
                    _lq = input("This activity is not found in your list. \n"
                                "please enter it's 'likeness':\n")
                    print("Registering...")
                    _lq = int(_lq)
                    # saving into dictionary
                    ActivitiesDic[str(_q)] = int(_lq)
                    tempFile = open("ActiDict.pkl", "wb")
                    pick.dump(ActivitiesDic, tempFile)
                    tempFile.close()
                    # printing results
                    loadfile("ActiDict.pkl")
                    print("Success!")
                    break
                except ValueError:
                    print("Please put an integer (aka whole number)")
            t += 1
            
    # Perform arrange_activities function
    arrange_activities()
    print(ActivitiesList)
    # Saving the organised schedule to hard drive
    print("Do you want to save the changes to the hard drive? (Y/N))")
    nqna = input()
    if nqna == "Y" or nqna == "y":
        hardSave()
    elif nqna == "N" or nqna == "n":
        print("Saving canceled")
    else:
        error("Cannot understand answer")
    


def arrange_activities():
    # Sort All activities
    sortedd = dict(sorted(ActivitiesDic.items(), key=operator.itemgetter(1), reverse=True))
    # Add in Moring mandatory activities
    for i in FixedActivitiesDict1.keys():
        ActivitiesList.append(i)
    # Add in the Morning Activities
    for i in sortedd.keys():
        a = 1
        if a != 6:
            ActivitiesList.append(i)
        a+=1
        
        if a >= 6:
            break
    # Add in Manditory After noon Activities
    for i in FixedActivitiesDict2.keys():
        ActivitiesList.append(i)
    # Add in After noon Activities
    for i in sortedd.keys():
        a = 7
        if a != 14:
            ActivitiesList.append(i)
        a+=1

        if a >= 13:
            break
    # Add in Manditory night Activities
    for i in FixedActivitiesDict3.keys():
        ActivitiesList.append(i)
    # Add in Night-time Activities
    for i in ActivitiesDic.keys():
        a = 14
        if a != 16:
            ActivitiesList.append(i)
        
        if a >= 16:
            break


def loadfile(filename):
    tempFile = open(str(filename), "rb")
    tempOut = pick.load(tempFile)
    print(tempOut)


def remove(_arg1):
    print("Starting Removal of" + _arg1)
    ActivitiesList.remove(_arg1)
    print("Removal Success!")
    print("Do you want to save the changes to the hard drive? (Y/N))")
    _rqna = input()
    if _rqna == "Y" or _rqna == "y":
        print("Starting Save")
        print("which file would you want to assign the change?")
        _sqna = input()
        pick.dump(ActivitiesList, open(_sqna + ".dat", "wb"))
        print("Saving Success!")
    else:
        print("Saving canceled")
    print(ActivitiesList)


def HardExit():
    print("Executing HardExit...")
    print("Execution Success!")
    print("Goodbye! Have a nice day!")
    exit()


def error(message):
    print(f"{Fore.RED} Error: " + str(message))


def test():
    for _i in range(10):
        print(f"{Fore.LIGHTBLUE_EX}" + "hi", end="")


def welcomeScreen():
    print(f"{Fore.LIGHTBLUE_EX}" + figlet_format("Asg", font="Big"))
    print(f"{Fore.LIGHTBLUE_EX}" + figlet_format("Automated Schedule Generators", font="Mini"))
    print(f"{Fore.LIGHTMAGENTA_EX}" + "Hi! Welcome to ASG".center(80, "=") + "\n" + f"{Fore.BLUE}" +
          "Your place to get organised".center(80, "="))


def about():
    print("This is a thing made by Anonymous Leo")


welcomeScreen()  # Welcoming!

# Main Loop
while True:
    # Start Program and preps!
    if os.path.getsize("ActiDict.pkl") > 0:
        with open("ActiDict.pkl", "rb") as f:
            ActivitiesDic = pick.load(f)
    

    print("Today is " + WeekDay + "\nWhat do you need? \n( /help to get all commands )")
    command = input()
    if command == "/help":
        for _i in range(36):
            print(f"{Fore.GREEN}=", end="")
        print(f"{Fore.GREEN} COMMANDS ", end="")
        for _i in range(36):
            print(f"{Fore.GREEN}=", end="")
        print(f"{Fore.LIGHTGREEN_EX}\n/new : to create your schedule, \n"
              "/move acc 'obj arg' 'time arg' : move the selected activity to another time (Still in developpment), \n"
              "/remove acc 'obj arg' : delete or remove the selected activity, \n"
              "/save acc 'name arg' : saves the current activity into your hard drive and read it later, \n"
              "/load acc 'name arg' : loads the selected schedule from the hard drive, \n"
              "/x or /exit : Stops the programs, \n"
              "/test : Applies what ever is the test, \n"
              "/About : Know more about this program! \n"
              "/devmode : Show hidden errors")


    elif command == "/new":
        new()

    elif command == "/remove":
        print("What do you want to remove? \n (" + str(ActivitiesList) + ") \n")
        crqna = input()
        remove(crqna)

    elif command == "/save":
        hardSave()

    elif command == "/load":
        hardLoad()

    elif command == "/x" or command == "/exit":
        HardExit()

    elif command == "/test":
        test()

    elif command == "/about":
        about()

    elif command == "/devmode":
        if devMode:
            devMode = False
        else:
            devMode = True
        print(f"{Fore.LIGHTBLUE_EX}Dev mode: %s" % devMode)
    else:
        error("Unknown command (" + command + ")")

# By AGhosylyCoder