# A Script to lauch your favorite apps.

# Import librares --

from pathlib import Path

# Explict imports to satisfy Flake8
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog
import os
from PIL import ImageTk, Image

#---------------------

###### Path #######

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\DATA_02\GitHub_Repo\Launch\assets\frame0")

##############################


# Main Program --

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def keep_flat(event):      
    if event.widget is button_1 or button_2 or button_3: 
        event.widget.config(relief="flat") 




######### UI #############

window = Tk()

window.geometry("800x500")
window.configure(bg = "#2D2D2D")

apps = []


if os.path.isfile('config.txt'):
    with open('config.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]      # Check Config File as the app starts.

# Button def --

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", 
    filetypes=(("Executables", "*.exe"), ("All Files", "*.*")))
    apps.append(filename)
    for app in apps:
        lable = tk.Label(frame, text=app)
        lable.pack()

def run_apps():
    for app in apps:
        os.startfile(app)

# -------------------------


canvas = Canvas(
    window,
    bg = "#2C2C2C",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=addApp,
    relief="flat"
)
button_1.place(
    x=607.0,
    y=120.0,
    width=144.0,
    height=39.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    highlightcolor="#2D2D2D",
    command=run_apps,
    relief="flat"
)
button_2.place(
    x=607.0,
    y=262.0,
    width=144.0,
    height=39.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,
    relief="flat"
)
button_3.place(
    x=607.0,
    y=405.0,
    width=144.0,
    height=39.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    274.0,
    282.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    102.0,
    38.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    242.0,
    91.0,
    image=image_image_3
)

frame = tk.Frame(window)
frame.place(anchor="center", relx=0.342, rely=0.564)

img = ImageTk.PhotoImage(Image.open(r"E:\DATA_02\GitHub_Repo\Launch\assets\frame0\image_1.png"))

label = tk.Label(frame, borderwidth=0)
label.pack()

window.bind('<Button-1>', keep_flat)

for app in apps:
    lable = tk.Label(frame, text=app)
    lable.pack()

window.resizable(False, False)
window.mainloop()

############################################

with open('config.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')

#-----------------------------------