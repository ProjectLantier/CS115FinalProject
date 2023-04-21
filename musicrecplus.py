#Lauren Kibalo, Eshan Sharma, Bryce Lu
#I pledge my honor that I have abided by the Stevens Honor System - Lauren, Eshan, Bryce

import functools

FILE = "musicrecplus.txt"


def fileData(filename):
    """ Converting text file into a dictionary """
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
