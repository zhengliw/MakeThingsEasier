#!/bin/python3

# MakeThingsEasier - mte
# A command line utility, more in the README

from os import system

configFile = open("keyconfig.txt", "r") # Open the key config file in read-only mode
config = dict() # Load configurations

for line in configFile: # for each line in configFile
    configLine = line.split('=') # read the key and value...
    config[configLine[0]] = configLine[1] # set key to value

try:
    while True:
        action = input(">>> ") # get user input to know what the user wants to do
        if action != '': # only do something if the user really typed something
            try:
                system(config[action]) # do the action
            except KeyError: # if the action is not defined
                print("The action is not defined.") # screw it
except KeyboardInterrupt: # if user wants to leave
    configFile.close() # close file
    print("\nBye bye :)") # bye guy