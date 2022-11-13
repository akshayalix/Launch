# A Script to lauch your favorite apps.

# Import librares --

from pathlib import Path

# Explict imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os

#---------------------

###### Path #######

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\aksha\Desktop\build\assets\frame0")

##############################


# Main Program --

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#-----------------------------------