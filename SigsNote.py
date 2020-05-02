from tkinter import *

# GUI and it's settings
window = Tk()
window.configure(background="black")
window.geometry("400x400+400+200")

# Main frame of the program
theFrame = Frame(window)
theFrame.pack(fill=BOTH, expand=True)

# Text field
textField = Text(theFrame, bg="black", fg="orange")
textField.pack()

# Drop down menus
theMenu = Menu(window)
window.config(menu=theMenu)

theFirstDropDown = Menu(theMenu, tearoff=0)
theMenu.add_cascade(label="File", menu=theFirstDropDown)
theFirstDropDown.add_command(label="Open")
theFirstDropDown.add_command(label="Save")
theFirstDropDown.add_command(label="Save as...")
theFirstDropDown.add_separator()
theFirstDropDown.add_command(label="Exit", command=window.quit)

theSecondDropDown = Menu(theMenu, tearoff=0)
theMenu.add_cascade(label="Edit", menu=theSecondDropDown)
theSecondDropDown.add_command(label="Copy")
theSecondDropDown.add_command(label="Paste")
theSecondDropDown.add_command(label="Search")
theSecondDropDown.add_command(label="Clear")

theThirdDropDown = Menu(theMenu, tearoff=0)
theMenu.add_cascade(label="Help", menu=theThirdDropDown)
theThirdDropDown.add_command(label="Help")
theThirdDropDown.add_command(label="About")

# Keeps the program running
window.mainloop()