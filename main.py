#!/bin/python3

# MakeThingsEasier - mte
# A command line utility, more in the README

from os import system # for command running
from sys import argv  # for command-line arguments

###

def runAction(keyconfig, action): # function for running the action
    '''Runs the action defined by keyconfig.
    Returns True if action is defined in keyconfig and being run with system(),
    returns False if action is not defined and not being run with system()'''

    if action != '': # only do something if the user really typed something
        try:
            system(keyconfig[action]) # do the action
        except KeyError: # if the action is not defined
            print("The action is not defined.")
            return False

    return True # everything worked lol

###

runFromArgvSuccess = False # initialize as bool

###

keyconfigFile = open("keyconfig.txt", "r") # Open the key keyconfig file in read-only mode
keyconfig = dict() # Load keyconfigurations

for line in keyconfigFile: # for each line in keyconfigFile
    keyconfigLine = line.split('=') # read the key and value...
    keyconfig[keyconfigLine[0]] = keyconfigLine[1] # set key to value

###

if len(argv) != 1: # if there is a command line argument
    runFromArgvSuccess = runAction(keyconfig, argv[1]) # try to use command line

try:
    while not runFromArgvSuccess: # if running action from argv failed or no argv passed at all
                                  # so runFromArgvSuccess stays False
        action = input(">>> ") # get user input to know what the user wants to do
        runAction(keyconfig, action)
except KeyboardInterrupt: # if user wants to leave
    keyconfigFile.close() # close file
    print("\nBye bye :)") # bye guy