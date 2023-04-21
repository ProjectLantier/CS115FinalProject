#Lauren Kibalo, Eshan Sharma, Bryce Lu
#I pledge my honor that I have abided by the Stevens Honor System - Lauren, Eshan, Bryce

import functools

FILE = "musicrecplus.txt"


def fileData(filename):
    """ Converting text file into a dictionary """
    #Lauren

    dict = {}
    with open(filename) as f:
        if f == "":
            return {}
        for line in f:
            (key, val) = line.split(":")
            dict[key] = val
    global dictGlobal
    dictGlobal = dict
    return dict

def menu():
    print("""Enter a letter to choose an option:
e - Enter preferences
r - Get recommendations
p - Show most popular artists
h - How popular is the most popular
m - Which user has the most likes
q - Save and quit""")

def saveQuit():
    """ Saves the dictionary to the text file """
    #Lauren

    with open(FILE, 'w') as f:
        for key in dictGlobal.keys():
            f.write("%s:%s" % (key, dictGlobal[key]))
    print("Preferences saved to", FILE, "Have a nice day!")
    quit()
    

def userChoice():
    """ Provides the user menu options """
    #Lauren, Eshan, Bryce

    choices = input("Enter a letter to choose an option :\n e - Enter preferences\n r - Get recommendations\n p - Show most " \
           "popular artists\n h - How popular is the most popular\n m - Which user has the most likes\n d - Delete " \
           "Preferences\n s - Show Preferences\n q - Save and " \
           "quit\n")

    while choices != "q":

        if choices == "e":
            #enterPref()
        elif choices == "r":
            #getRec()
        elif choices == "p":
            #showPop()
        elif choices == "h":
            #popMost()
        elif choices == "m":
            #mostLikes()
        elif choices == "q":
            saveQuit()
        else:
            choices = input("Enter a letter to choose an option :\n e - Enter preferences\n r - Get recommendations\n p - Show most " \
           "popular artists\n h - How popular is the most popular\n m - Which user has the most likes\n d - Delete " \
           "Preferences\n s - Show Preferences\n q - Save and " \
           "quit\n")
        



