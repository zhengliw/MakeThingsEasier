# MakeThingsEasier - mte

A command line utility/python script to speed up your workflow. After a mte shell is opened, just type a letter/word/whatever man (afterwards keyconfigurable) to open a browser, run a custom python script and more!

## Why this useless script?

Uh.. I hate to touch my mouse, it makes me unprofessional. And I hate having to type an essay when I just want to open my browser.

## How to use?

First, go to keykeyconfig.txt and change the actions according to your needs. On the left side of the equal sign (=), type the shortcut you want and on the right side, type what should be executed in the terminal. **Don't add spaces around the equal sign.** More features upcoming!

## Program logic (v1.1 upwards)

Argv is yes if a command line argument is passed to the script.

Success is yes if the action is defined and could be run

Argv yes, Success yes: The program exits after executing action

Argv yes, Success no: The program shows an error message, then launches the normal mte shell

Argv no, Success yes/no: The program shows the mte shell until the user presses ctrl-c to exit