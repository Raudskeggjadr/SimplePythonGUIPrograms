import os
from tkinter import *

# GUI and it's settings
from tkinter import filedialog

window = Tk()
window.configure(background="black")
window.geometry("400x400+400+200")

# Main frame of the program
theFrame = Frame(window)
theFrame.pack(fill=BOTH, expand=True)

# Text field
textField = Text(theFrame, font="Helvetica 32", bg="black", fg="orange")
textField.pack(fill=BOTH, expand=True)


# Drop Down Menus functionality
def raze_it_to_the_ground():
    textField.delete("1.0", END)


def open_text_file():
    text_file_directory = filedialog.Open(initialdir=os.getcwd(),
                                          filetypes=(("Text Files", "*txt"), ("All Files", "*")))
    with open(text_file_directory.show(), "r") as hh:
        text = hh.read()
        raze_it_to_the_ground()
        textField.insert(0, text)


# Drop down menus
theMenu = Menu(window)
window.config(menu=theMenu)

theFirstDropDown = Menu(theMenu, tearoff=0)
theMenu.add_cascade(label="File", menu=theFirstDropDown)
theFirstDropDown.add_command(label="Open", command=open_text_file)
theFirstDropDown.add_command(label="Save")
theFirstDropDown.add_command(label="Save as...")
theFirstDropDown.add_separator()
theFirstDropDown.add_command(label="Exit", command=window.quit)

theSecondDropDown = Menu(theMenu, tearoff=0)
theMenu.add_cascade(label="Edit", menu=theSecondDropDown)
theSecondDropDown.add_command(label="Copy")
theSecondDropDown.add_command(label="Paste")
theSecondDropDown.add_command(label="Search")
theSecondDropDown.add_command(label="Clear", command=raze_it_to_the_ground)

theThirdDropDown = Menu(theMenu, tearoff=0)
theMenu.add_cascade(label="Help", menu=theThirdDropDown)
theThirdDropDown.add_command(label="Help")
theThirdDropDown.add_command(label="About")

# Keeps the program running
window.mainloop()
