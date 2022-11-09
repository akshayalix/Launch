# A script to launch various utility service application on machine.

# Import Dependencies -- 

import os
import ctypes

#........................

# Global variables --

global CurrentVersion
global author
global title

#.........................

# Global def --

CurrentVersion = "0.1"

author = "Alix"

title = "Launch-er"

ctypes.windll.kernel32.SetConsoleTitleW(title + " v" + str(CurrentVersion))

#............................

# Main Script --

print("=====================")
print("=                   =")
print("=      Welcome      =") 
print("=                   =")
print("=====================")

