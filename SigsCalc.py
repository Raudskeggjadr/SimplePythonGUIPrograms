from tkinter import *
# from tkinter import filedialog

# Parent Class for all the buttons
class ButtonsClass:
    def __init__(self, master, x, xx, xxx):
        self.x = x
        self.xx = xx
        self.xxx = xxx

        Grid.rowconfigure(master, x, weight=1)
        Grid.columnconfigure(master, xx, weight=1)

        aButton = Button(master, text=" "+str(xxx)+" ", font="helvetica 20", bg="black", fg="yellow")
        aButton.grid(row=x, column=xx, sticky="nsew")

# GUI and it's setting
window = Tk()
window.configure(background="black")
window.geometry("400x400+400+200")

# Main frame of the programm
theFrame = Frame(window)
theFrame.pack(fill=BOTH, expand=True)

# Numbers field
theNumbers = StringVar()
theNumbers.set(0)
theField = Label(theFrame, textvariable=theNumbers, anchor="e", font="Helvetica 56", bg="black", fg="orange")
theField.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Function buttons - number buttons
a = ButtonsClass(theFrame, 1, 0, 1)
b = ButtonsClass(theFrame, 1, 1, 2)
c = ButtonsClass(theFrame, 1, 2, 3)
d = ButtonsClass(theFrame, 2, 0, 4)
e = ButtonsClass(theFrame, 2, 1, 5)
f = ButtonsClass(theFrame, 2, 2, 6)
g = ButtonsClass(theFrame, 3, 0, 7)
h = ButtonsClass(theFrame, 3, 1, 8)
i = ButtonsClass(theFrame, 3, 2, 9)

# Keeps the program running
window.mainloop()
