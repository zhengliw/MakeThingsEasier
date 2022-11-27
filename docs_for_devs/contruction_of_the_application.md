This file is a work-in-progress file...

# Contruction of the application

### ...(for the next version (v.1.4.0 upwards))

[The original GitHub repository, along with the license](https://github.com/zhengliw/MakeThingsEasier)

Hi! I think that you are also sick and tired of all these undocumented repositories. So here I am.

I will try to implement the "50% code, 50% documentation" philosophy in this repository. Have fun!

### Firstly...

Like every application, there are call levels or so I call them. There is a ***runner file (Level 1)*** that initializes all the modules and calls the methods and functions from the modules. In our case probably: `main.py`.

One level below the runner, you can find the ***actual modules (Level 2.1)***. I bet you noticed that I used the number 2.1 instead of the integer 2 for the modules. The reason is simple: On the same level, there are ***config files (Level 2.2)*** with help of which the end user can modify the behavior of the software/program/whatever without having to change the actual source code.

And below those, you can find the ***dependencies (Level 3)***. These are pieces of code/software that are not maintained by me (lol, everybody knows that appearently). Still, my program/software or even my own modules need these dependencies to run. Dependencies could be additional libraries/frameworks/modules/... from external developers, but also could be the runtime for the language itself, if it is an interpreted, non-compiled language (Python, in our case). The dependencies are installed apart from my program. Since we are using pure Python for this project: The package manager for Python (pip) handles such dependencies automatically as long as a `requirements.txt` is specified. In our case, it is not present right now because we are relying on the included libraries of Python. Python itself can be installed with an installer or a package manager like `apt`, `chocolatey` or `homebrew`.

I hope that I could explain a couple things concerning the context. Without further ado, let's run this down.

### Structure of the code of this program

| Level | Name      | Function                                       |
| ----- | --------- | ---------------------------------------------- |
| 1     | `main.py` | The runner that initializes all other modules. |
| 2.1   | ...       | ...                                            |
