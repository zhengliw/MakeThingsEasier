# MTE - MakeThingsEasier
# Licensed under the MIT License
# (c) Zhengli Wang
# More details at the root of this repository

# -------------------------
#    Universal variables
# -------------------------

# Document relevant variables
__name__ = "MTE - MakeThingsEasier"
__author__ = "Zhengli Wang"
__description__ = """MTE - A command-line shortcuts utility."""

# Execution relevant variables
configFilename = "config.txt"

# -------------
#    Imports
# -------------

# System libraries
import warnings
import configparser
import argparse
import os

# My custom libraries
import lib.cmd

# ----------------------
#    Argument parsing
# ----------------------

argumentParser = argparse.ArgumentParser(
    # Program name
    prog=__name__,
    # Program description
    description=__description__,
    # Add --help/-h flag
    add_help=True,
)

# Create an optional, positional argument for "quick mode" (see README)
argumentParser.add_argument(
    "action", action="store", default=None, nargs="*", help="Quick mode action."
)

# Create an optional, unpositional argument for specifying a config.txt for
# this run
argumentParser.add_argument(
    "--config-file",
    action="store",
    default=configFilename,
    required=False,
    nargs=1,
    help="Specify another config file than the default one for this run.",
    dest="configFile",
)

# Create a namespace object for the parsed args
argumentNamespace = argumentParser.parse_args()

# There are cases where you might want to execute a multi-parted,
# space-separated command with quick mode. Since argparse writes
# such commands into a list, we will rejoin it back with this line
# of code.
argumentNamespace.action = " ".join(argumentNamespace.action)

# Use the overridden config file
configFilename = argumentNamespace.configFile

# --------------------
#    Config parsing
# --------------------

defaultConfig = {"exitAfterArgvSuccess": 1, "showIntro": 1, "showWarnings": 0}

configParser = configparser.ConfigParser()

# Bypass lowercasing of optionxform, preserving
# case-sensitvity
configParser.optionxform = str

# Load in default config
configParser["config"] = defaultConfig.copy()

# Overwrite default config
configParser.read(configFilename)

config = configParser["config"]
keyconfig = configParser["keyconfig"]

# -----------------------------------------------
#    Command-line-like interface configuration
# -----------------------------------------------

# Special actions which are not defined in
# keyconfig
customActions = {"help": help, "exit": exit}

# All actions, including the keys in
# keyconfig
allActions = list(customActions.keys()) + list(keyconfig.keys())


def help():

    """
    List all available commands. This is used for the
    interactive MTE shell.
    """

    print("Available commands: ")

    # List all commands in form of:
    # 'command1' 'command2' 'command3'...
    for command in allActions:
        print("'" + command + "'", end=" ")

    # New line
    print("")


def runAction(action: str):

    """
    Try to run action. If KeyError, print message and warn.

    Returns 0 on success, returns 1 on failure.
    """

    try:
        os.system(keyconfig[action])
    except KeyError:
        print(
            "This action is probably not defined. Enter 'help' to list available commands."
        )
        warnings.warn("Action not defined: " + action)
        return 1
    else:
        return 0


commandLine = lib.cmd.Cmd(
    runAction,
    intro=__name__,
    showIntro=(config["showIntro"] == "1"),
    customActions={"help": help, "exit": exit},
)

# -------------------------
#    Misc configurations
# -------------------------

if config["showWarnings"] == "0":
    warnings.filterwarnings("ignore")

# ------------------------------------------------------
#    Quick mode (the code might end after this block)
# ------------------------------------------------------

# Try to start in quick mode

# If quick mode succeeds, exit the program if
# config["exitAfterArgvSuccess"] is set to '1'

try:
    # Make sure that there is an action at all
    if argumentNamespace.action:
        if runAction(argumentNamespace.action) == 0:
            if config["exitAfterArgvSuccess"] == "1":
                exit(0)
except ValueError:
    pass

commandLine.cmdloop()
