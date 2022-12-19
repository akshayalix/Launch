# A new script for lauching specified apps with startup.

# Libs
import os
from time import sleep
#______________

# Variables

def rapoo():
    rap = r'C:\Program Files (x86)\Rapoo Audio 7.1\Rapoo Audio 7.1.exe'
    os.startfile(rap)

    # For Rapoo Sound.

def mica():
    mica = r'C:\Program Files (x86)\Mica For Everyone\MicaForEveryone.exe'
    os.startfile(mica)

    # For Mica.

def power():
    toys = r'C:\Program Files\PowerToys\PowerToys.exe'
    os.startfile(toys)

    # For PowerToys.