#Lauren Kibalo, Eshan Sharma, Bryce Lu
#I pledge my honor that I have abided by the Stevens Honor System - Lauren, Eshan, Bryce

import functools
from ast import Compare

filename = "musicrecplus.txt"


def fileData(filename):
    """ Converting text file into a dictionary """
    #Lauren
    dict = {}
    with open(filename) as f:
        if f == "":
            return {}
        for line in f:
            (userName, artist) = line.split(":")
            dict[userName] = artist
    global dictGlobal
    dictGlobal = dict
    return dict

def checkName():
    """Checks if the input user name is in the database, if not return false, if true add to database"""
    #Bryce
    global myName
    while myName == "":
        myName = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    if myName not in dictGlobal:
        dictGlobal[myName] = []
        # print("changed database:")
        # print(database)
        return False
    return True

def isPrivate(s):
    """Returns true if the username s has a $ at the end of it"""
    #Bryce
    if s[-1] == "$":
        return True
    else:
        return False

def enterPreferences():
    """Lets the user enter their artist preferences until they enter an empty string"""
    #Bryce
    x = "0"
    while x != "":
        x = input("Enter an artist that you like (Enter to finish): \n")
        if x == "":
            break
        else: 
            dictGlobal[userName] += [(x)]
    return userChoice()
     
def menu():
    #Eshan
    print("""Enter a letter to choose an option:
e - Enter preferences
r - Get recommendations
p - Show most popular artists
h - How popular is the most popular
m - Which user has the most likes
q - Save and quit""")
    
def mostPopular():
    """ Displays the artist with the most likes, user option h """
    #Lauren

    partP = showPopular() #assuming part p makes a dictionary of low to high popular artists


    if partP != {}:
        for artist in partP:
            if partP[artist] >= mostPopular:
                mostPopular = partP[artist]
                mostPopularArtist = artist
            print("The most popular artist is", mostPopularArtist)
    else:
        return userChoice()


def saveQuit():
    """ Saves the dictionary to the text file, user option q """
    #Lauren

    with open(FILE, 'w') as f:
        for key in dictGlobal.keys():
            f.write("%s:%s" % (key, dictGlobal[key]))
    print("Your preferences have been saved to:", FILE)
    quit()

def deletePreferences():
    """ Deletes the user's preferences, user option d """
    #Eshan
    dictGlobal[userName] = []
    return userChoice()

def showPreferences(userName):
    """ Display user preferences, user option s """
    #Bryce
    print(dictGlobal[userName])

def showPopular():
    """Shows the most popular artists in the database"""
    #Eshan
    artistDict = {}
    for key in dictGlobal.keys():
        for artist in dictGlobal[key]:
            if artist in artistDict:
                artistDict[artist] += 1
            else:
                artistDict[artist] = 1
    return artistDict
    
def getRecommendations():
    """Gives the user recommendations based on the preferences they input"""
    #Eshan
    artistDict = showPopular()
    for artist in dictGlobal[userName]:
        if artist in artistDict:
            del artistDict[artist]
    sortedArtistDict = sorted(artistDict.items(), key=functools.cmp_to_key(Compare))
    for artist in sortedArtistDict:
        print(artist[0])
    return userChoice()
   
def mostLikes():
    """Shows the user which artist has the most likes according to the database"""
    #Eshan
    artistDict = showPopular()
    sortedArtistDict = sorted(artistDict.items(), key=functools.cmp_to_key(Compare))
    print(sortedArtistDict[0][0])
    return userChoice()
def userChoice():
    """ Provides the user menu options """
    #Lauren

    choices = input("Enter a letter to choose an option :\n e - Enter preferences\n r - Get recommendations\n p - Show most " \
           "popular artists\n h - How popular is the most popular\n m - Which user has the most likes\n d - Delete " \
           "Preferences\n s - Show Preferences\n q - Save and " \
           "quit\n")

    while choices != "q":

        if choices == "e":
            enterPreferences()
        elif choices == "r":
            getRecommendations()
        elif choices == "p":
            showPopular()
        elif choices == "h":
            mostPopular()
        elif choices == "m":
            mostLikes()
        elif choices == "d":
            deletePreferences()
        elif choices == "s":
            showPreferences()
        elif choices == "q":
            saveQuit()
        else:
            choices = input("Enter a letter to choose an option :\n e - Enter preferences\n r - Get recommendations\n p - Show most " \
           "popular artists\n h - How popular is the most popular\n m - Which user has the most likes\n d - Delete " \
           "Preferences\n s - Show Preferences\n q - Save and " \
           "quit\n")
        
