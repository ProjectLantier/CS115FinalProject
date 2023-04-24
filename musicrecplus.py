#Lauren Kibalo, Eshan Sharma, Bryce Lu
#I pledge my honor that I have abided by the Stevens Honor System - Lauren, Eshan, Bryce

import functools
import operator

FILE = "musicrecplus_ex2_a.txt"


def fileData(filename):
    """ Converting text file into a dictionary """
    #Lauren
    open(filename,"a")
    file = open(filename, "r")
    userDictionary = {}
    for line in file:
        [username,artist] = line.strip().split(":")
        artistList = artist.split(",")
        artistList.sort()
        userDictionary[username] = artistList
    file.close()
    return userDictionary

def enterPreferences(username, userDictionary):
    """Lets the user enter their artist preferences until they enter an empty string"""
    #Bryce
    prefList = []
    while True:
        artistInput = input("Enter an artist that you like (Enter to finish):\n")
        if not artistInput:
            break
        prefList += [artistInput]
    prefList = map(lambda x: x.title(),prefList)
    prefList.sort()
    userDictionary[username]=prefList

def deletePreferences(username, userDictionary):
    """ Deletes the user's preferences """
    #Eshan
    if username in userDictionary:
        del userDictionary[username]
    else:
        print("Sorry, no preferences found for " + username)

def showPreferences(username, userDictionary):
    """ Shows the user's preferences """
    #Bryce
    if username in userDictionary:
        print("Preferences for " + username + ":")
        for artist in userDictionary[username]:
            print(artist)
    else:
        print("Sorry, no preferences found for " + username)

def getRecommendations(username, userDictionary):
    """Gives the user recommendations based on the preferences they input"""
    #Eshan
    current=["",0]
    for key in userDictionary:
        if not(key[-1]=="$"):
            val = compare(userDictionary[username],userDictionary[key],0)
            if (val>current[1] and not(userDictionary[key]==userDictionary[username])):
                current=[key,val]
    recommendationsList=[]
    if not(current[0]==""):
        for item in userDictionary[current[0]]:
            if not(item in userDictionary[username]):
                recommendationsList+=[item]
    if not(recommendationsList==[]):
        for i in recommendationsList:
            print(i)
    else:
        print("No recommendations available at this time.")

            
def mostPopular(userDictionary):
    """ Displays the artist with the most likes, user option h """
    #Lauren
    count = showPopular(userDictionary,True)
    if count == 0:
        print("Sorry, no artists found.")
    else:
        print(count)

def showPopular(userDictionary,amountPopBool):
    """Shows the most popular artists in the database"""
    #Eshan
    artistDictionary={}
    for key in userDictionary:
        if not(key[-1]=="$"):
            for item in userDictionary[key]:
                if item in artistDictionary:
                    artistDictionary[item]+=1
                else:
                    artistDictionary[item]=1
    popularArtistList=[["",0],["",0],["",0]]
    for artist in artistDictionary:
        currentArtist=artistDictionary[artist]
        for i in range(3):
            if currentArtist>popularArtistList[i][1]:
                popularArtistList[i]=[artist,currentArtist]
                break
    if amountPopBool:
        return popularArtistList[0][1]
    else:
        if popularArtistList[0][1]==0:
            print("Sorry, no artists found.")
        else:
            for i in range(3):
                print(popularArtistList[i][0])

def mostLikes(userDictionary):
    """Shows the user which artist has the most likes according to the database"""
    #Eshan
    mostLikes = [0,""]
    for key in userDictionary:
        if not(key[-1]=="$"):
            if len(userDictionary[key])>mostLikes[0]:
                mostLikes = [len(userDictionary[key]),key]
    if mostLikes[0]==0:
        print("Sorry, no artists found.")
    else:
        print(mostLikes[1])


def saveQuit(fileName, userDictionary):
    """ Saves the dictionary to the text file, user option q """
    #Lauren

    newDict = sortDictionary(userDictionary)
    newFile = open(fileName,"w")
    for key in newDict:
        S = str(key) + ":" + ",".join(newDict[key]) + "\n"
        newFile.write(S)
    newFile.close()


def compare(val1,val2,sameVal):
    #Eshan
    "Returns amount of common artists between two users preferences"
    if (val1==[] or val2==[]):
        return sameVal
    elif val1[0]<val2[0]:
        return compare(val1[1:],val2,sameVal)
    elif val1[0]==val2[0]:
        return compare(val1[1:],val2[1:],sameVal+1)
    else:
        return compare(val1,val2[1:],sameVal)

def userChoice(userDictionary):
    """ Provides the user menu options """
    #Lauren
    
    nameInput = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):\n")
    nameInput=nameInput.title()
    if not(nameInput in userDictionary):
        enterPreferences(nameInput,userDictionary)
    while True:
        optionLetter = input("""Enter a letter to choose an option:\ne - Enter preferences\nd - Delete preferences\ns - Show preferences \nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit\n""")
        if(optionLetter=="e"):
            enterPreferences(nameInput,userDictionary)
        elif(optionLetter=="d"):
            deletePreferences(nameInput,userDictionary)
        elif(optionLetter=="s"):
            showPreferences(nameInput,userDictionary)
        elif(optionLetter=="r"):
            getRecommendations(nameInput,userDictionary)
        elif(optionLetter=="p"):
            showPopular(userDictionary, False)
        elif(optionLetter=="h"):
            mostPopular(userDictionary)
        elif(optionLetter=="m"):
            mostLikes(userDictionary)
        elif(optionLetter=="q"):
            saveQuit(FILE,userDictionary)
            break
    return userDictionary

def sort(userDictionary):
    """ Sorts the dictionary by key """
    #Lauren
    L = []
    for i in userDictionary:
        L += [i]
    L.sort()
    return L

def sortDictionary(userDictionary):
    """ Sorts the dictionary by key """
    #Eshan
    L = sort(userDictionary)
    newFile = {}
    for i in L:
        newFile[i] = userDictionary[i]
    return newFile

def map(function, sequence):                #From CS115
    '''map(function, sequence) -> list
       Like list(map(...)) in Python 3.'''
    return [function(x) for x in sequence] if function != None \
        else [item for item in sequence if item]


def __helprange(start, end, step=1):        #From CS115
    lst = []
    if step < 0:
        while start > end:
            lst += [start]
            start += step
    elif step > 0:
        while start < end:
            lst += [start]
            start += step
    else:
        raise ValueError('range() step argument cannot be zero.')
    return lst

def range(*args):                    #From CS115
    '''range(stop) -> list of integers
       range(start,stop[,step]) -> list of integers
       Like list(range(...)) in Python 3.'''
    num_args = len(args)
    if num_args == 1: return __helprange(0, args[0])
    if num_args == 2: return __helprange(args[0], args[1])
    if num_args == 3: return __helprange(args[0], args[1], args[2])
    raise TypeError('range() must have 1, 2, or 3 arguments.')

def main():
    userDictionary = fileData(FILE)
    userChoice(userDictionary)

if __name__=="__main__":
    main()
