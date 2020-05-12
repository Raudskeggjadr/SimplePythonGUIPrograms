import os
from tkinter import *

# GUI and it's settings
from tkinter import filedialog, messagebox

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
        textField.insert("1.0", text)


def save_text_file_as():
    if textField.get("1.0", END) != "":
        new_text_file_firectory = filedialog.asksaveasfilename(initialdir=os.getcwd(),
                                                               filetypes=(("Text Files", "*txt"), ("All Files", "*")),
                                                               defaultextension=".txt")
        with open(new_text_file_firectory, "w") as kk:
            kk.write(textField.get("1.0", END))
            kk.close()


def help_window():
    messagebox.showinfo("Help", "This is a help window.")


def about_window():
    messagebox.showinfo("About", "Created by Zygmunt Mocek")

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(textField.get(1.0, END))
    print(window.clipboard_get())

def paste_from_clipboard():
    textField.insert(END, window.clipboard_get())


# Drop down menus
theMenu = Menu(window)
window.config(menu=theMenu)

theFirstDropDown = Menu(theMenu, tearoff=0)
theMenu.add_cascade(label="File", menu=theFirstDropDown)
theFirstDropDown.add_command(label="Open", command=open_text_file)
theFirstDropDown.add_command(label="Save (WIP)")
theFirstDropDown.add_command(label="Save as...", command=save_text_file_as)
theFirstDropDown.add_separator()
theFirstDropDown.add_command(label="Exit", command=window.quit)

theSecondDropDown = Menu(theMenu, tearoff=0)
theMenu.add_cascade(label="Edit", menu=theSecondDropDown)
theSecondDropDown.add_command(label="Copy", command=copy_to_clipboard)
theSecondDropDown.add_command(label="Paste", command=paste_from_clipboard)
theSecondDropDown.add_command(label="Search (WIP)")
theSecondDropDown.add_command(label="Clear", command=raze_it_to_the_ground)

theThirdDropDown = Menu(theMenu, tearoff=0)
theMenu.add_cascade(label="Help", menu=theThirdDropDown)
theThirdDropDown.add_command(label="Help", command=help_window)
theThirdDropDown.add_command(label="About", command=about_window)

# Keeps the program running
window.mainloop()
