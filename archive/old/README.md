# MakeThingsEasier - mte

A command line utility/python script to speed up your workflow. After a mte shell is opened, just type a letter/word/whatever man (afterwards configurable) to open a browser, run a custom python script and more!

## Why this useless script?

Uh.. I hate to touch my mouse, it makes me unprofessional. And I hate having to type an essay when I just want to open my browser.

## How to use?

First, go to keyconfig.txt and change the actions according to your needs. On the left side of the equal sign (=), type the shortcut you want and on the right side, type what should be executed in the terminal. **Don't add spaces around the equal sign.**

Then, execute main.py (name can vary) to get to the interactive MTE shell to use your defined action shortcuts.

-or-

Directly run an action quickly by simply passing a command-line argument: 'python main.py your-command'. This method closes MTE immediately after a successful action run. I'll call it "Quick Mode".

## Program logic (v1.1 upwards)

Normally, the program will launch the normal MTE shell if the action passed through by the command-line argument isn't defined. This allows you to check if you made typos when using the command-line arguments. You can modify this behavior by going into config.txt and modifying exitAfterArgvSuccess.