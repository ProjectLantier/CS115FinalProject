#Lauren Kibalo, Eshan Sharma, Bryce Lu
#I pledge my honor that I have abided by the Stevens Honor System - Lauren, Eshan, Bryce

import functools

FILE = "musicrecplus.txt"


filename = "musicrecplus.txt"

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