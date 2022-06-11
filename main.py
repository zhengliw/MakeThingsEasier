#!/bin/python3

# MakeThingsEasier - mte
# A command line utility, more in the README

###
# Importing needed libs
###

from os import system # for command running
from sys import argv  # for command-line arguments

###
# The APIs
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

def readConfig(filename): # config reading function
    configFile = open(filename, "r") # Open the config file in read-only mode
    config = dict() # Load configurations

    for line in configFile: # for each line in configFile
        if line[0] != '#' and '=' in line: # only read key and value if the line is not a comment line
                                           # or trash line (no equal sign in line)
            configLine = line.split('=') # read the key and value...
            config[configLine[0]] = configLine[1] # set key to value

    configFile.close()
    return config

###
# Defining the variables that require pre-definining for the use case
###

runFromArgvSuccess = False # store if running the action from argv succeeded

###
# Reading the configurations
###

keyconfig = readConfig("keyconfig.txt")
generalconfig = readConfig("config.txt")

###
# "Actual code"
###

if len(argv) != 1: # if there is a command line argument
    runFromArgvSuccess = runAction(keyconfig, argv[1]) # try to use command line

try:
    # if running action from argv failed or no argv passed at all
    # so runFromArgvSuccess stays False
    # AND the config.txt says exitAfterArgvSuccess is 0
    while not runFromArgvSuccess and generalconfig['exitAfterArgvSuccess'] == '0': 
        action = input(">>> ") # get user input to know what the user wants to do
        runAction(keyconfig, action)
except KeyboardInterrupt: # if user wants to leave
    print("\nBye bye :)") # bye guy