# cmd.py - A minimal, customized prompt class for
# creating a command-line-like app
# Bundled with MTE - MakeThingsEasier.
# Licensed under the MIT license.
# (c) Zhengli Wang

# https://www.github.com/zhengliw/makethingseasier

class Cmd:

    """
    A class aiming to imitiate the core functionalities 
    of the famous Python library cmd. This is not intended
    to replace it in any way, but to be customized for MTE.

    The class assumes that all strings that are input on
    on the command-line interface this class creates will 
    be sent to the same function. This means that all commands
    will be processed by the same function which you define,
    except for the help message.

    I love Octocats.
    """

    def __init__(
        self, 
        action,
        helpAction,
        exitAction = exit,
        intro: str | None = None, 
        prompt: str = ">>> ",
        showIntro: bool = True,
        helpCommand: tuple = ("?", "help"),
        exitCommand: tuple = ("exit", "quit")
        ):
        
        """
        action:     A function that takes one argument which is the 
                    command being input, as a string
        helpAction: A function without arguments that is called when 
                    one command out of helpCommand is entered
        exitAction: A function that is called if the command the user
                    entered is in exitCommand
        intro:      A string that will be printed when cmdloop is 
                    executed
        prompt:     The prompt for the user
        showIntro:  At the begin of the cmdloop, show intro, helpCommand
                    and exitCommand.
        helpCommand:The commands the user can enter in order to get
                    help. See helpAction.
        exitCommand:The commands the user can enter in order to exit
                    the program. See exitAction.
        """

        self.action = action
        self.helpAction = helpAction
        self.exitAction = exitAction
        self.intro = intro
        self.prompt = prompt
        self.showIntro = showIntro
        self.helpCommand = helpCommand
        self.exitCommand = exitCommand
    
    def cmdloop(self):
        
        """
        1. Print the intro if self.showIntro.

        2. Continously ask for user input, str.strip the user input
        and call cmd.action (which is defined with init).

        3. If the command entered is present in self.helpCommand,
        self.helpAction is called.
        The same goes for exitCommand and exitAction.

        4. Empty lines are skipped.

        5. This method stops at KeyboardInterrupt.
        """

        if self.showIntro:
            print(self.intro)
            print("For help, enter one of these commands: " + ', '.join(self.helpCommand))
            print("To exit, enter one of these commands: " + ', '.join(self.exitCommand))

        try:
            while True:
                userInput = input(self.prompt)
                userInput = userInput.strip()

                if userInput in self.helpCommand:
                    self.helpAction()
                elif userInput in self.exitCommand:
                    self.exitAction()
                elif userInput == '':
                    continue
                else:
                    self.action(userInput)
        except KeyboardInterrupt:
            pass