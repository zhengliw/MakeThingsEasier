**Not actively maintained - Just found out there is a bash command called alias**

# MakeThingsEasier - MTE

This is the utility to speeddddd up your workflow!

# Why?

Do you know that feeling of having to type `sudo apt update && sudo apt upgrade -y` every dang single time? No more!

Go to config.txt and write something under keyconfig!

For example: `up = sudo apt update && sudo apt upgrade -y`

Then, just use the script and do a quick `mte up` and boom, you're finished.

# How to use?

First, configure config.txt according to your needs.

Under `[keyconfig]`, go and tweak the shortcuts you want to use. On the left side of the equal sign, write the shortcut. On the right side, write the full command.

Then, either directly use `mte [action]` for quick mode or just type `mte` to get to an interactive shell, where you can then type the action you want to perform.

Quick mode usually quits the program right after the command is successfully run. This can be changed in config.txt.

# I hate reading code

No problem! I tried to document the code to the fullest I can and it turned out being pretty well documented. You can also rip some code for your own project, just maybe :)

# Why isn't this packaged like any other app?

I'm sorry for that. My skills right now are kind of limited, so I have to learn to package Python apps sometime in the very near future. I'm sure that you don't need to wait for long.
