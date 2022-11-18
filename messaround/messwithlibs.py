import configparser

configFile = configparser.ConfigParser()
configFile.optionxform = lambda option: option

configFile.read("keyconfig.txt")

config = configFile["config"]
keyconfig = configFile["keyconfig"]

print(config)
print(keyconfig)

""" for section in configFile:
    print(section + ": ")
    for key, value in configFile.items(section):
        print(key + ": " + value) """