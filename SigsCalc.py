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

        a_button = Button(master, text=" " + str(xxx) + " ", command=self.button_pressed, font="helvetica 20",
                          bg="black", fg="yellow")
        a_button.grid(row=x, column=xx, sticky="nsew")

    def button_pressed(self):
        the_numbers_read = theNumbers.get()
        if the_numbers_read == "0":
            theNumbers.set(self.xxx)
        else:
            new_number = the_numbers_read + self.xxx
            theNumbers.set(new_number)


# Child class for functional buttons
class FuncionalClass(ButtonsClass):
    def button_pressed(self):
        if theNumbers.get() == "0":
            print("Nothing to calculate.")
        elif theMemorizedNumbers.get() == "0":
            theMemorizedNumbers.set(theNumbers.get() + self.xxx)
            theNumbers.set(0)
            print(theMemorizedNumbers.get())
        else:
            theMemorizedNumbers.set(theMemorizedNumbers.get() + theNumbers.get() + self.xxx)
            theNumbers.set(0)
            print(theMemorizedNumbers.get())

# Child class for dot button
class DotClass(ButtonsClass):
    def button_pressed(self):
        if "." in theNumbers.get():
            print("Just one dot is enough.")
        else:
            theNumbers.set(theNumbers.get() + self.xxx)


# Child class for equals button (equation shows up as false error)
class EquationClass(ButtonsClass):
    def button_pressed(self):
        if theNumbers.get() == "0":
            print("Nothing to calculate.")
        elif theMemorizedNumbers.get() == "0":
            print("Nothing to calculate.")
        else:
            print(theMemorizedNumbers.get() + theNumbers.get())
            exec("equation = " + theMemorizedNumbers.get() + theNumbers.get(), globals())
            print(equation)
            theNumbers.set(equation)
            theMemorizedNumbers.set(0)


# GUI and it's setting
window = Tk()
window.configure(background="black")
window.geometry("400x400+400+200")

# Main frame of the programm
theFrame = Frame(window)
theFrame.pack(fill=BOTH, expand=True)

# Numbers field
theNumbers = StringVar()
theMemorizedNumbers = StringVar()
theNumbers.set(0)
theMemorizedNumbers.set(0)
theField = Label(theFrame, textvariable=theNumbers, anchor="e", font="Helvetica 56", bg="black", fg="orange")
theField.grid(row=0, column=0, columnspan=4, sticky="nsew")


# Drop down menus functionality
def ddm_copy():
    window.clipboard_clear()
    window.clipboard_append(theNumbers.get())
    print(window.clipboard_get())


def ddm_paste():
    theNumbers.set(str(window.clipboard_get()))


def raze_it_to_the_ground():
    theNumbers.set(0)


# Drop down menus
theMenu = Menu(window)
window.config(menu=theMenu)

firstDropDown = Menu(theMenu, tearoff=0)
theMenu.add_cascade(label="File", menu=firstDropDown)
firstDropDown.add_command(label="Open")
firstDropDown.add_command(label="Save")
firstDropDown.add_command(label="Save as...")
firstDropDown.add_separator()
firstDropDown.add_command(label="Exit", command=window.quit)

secondDropDown = Menu(theMenu, tearoff=0)
theMenu.add_cascade(label="Edit", menu=secondDropDown)
secondDropDown.add_command(label="Copy", command=ddm_copy)
secondDropDown.add_command(label="Paste", command=ddm_paste)
secondDropDown.add_command(label="Clear", command=raze_it_to_the_ground)

thirdDropDown = Menu(theMenu, tearoff=0)
theMenu.add_cascade(label="Help", menu=thirdDropDown)
thirdDropDown.add_command(label="Help")
thirdDropDown.add_command(label="About")

# Function buttons - number buttons
a = ButtonsClass(theFrame, 1, 0, "1")
b = ButtonsClass(theFrame, 1, 1, "2")
c = ButtonsClass(theFrame, 1, 2, "3")
d = ButtonsClass(theFrame, 2, 0, "4")
e = ButtonsClass(theFrame, 2, 1, "5")
f = ButtonsClass(theFrame, 2, 2, "6")
g = ButtonsClass(theFrame, 3, 0, "7")
h = ButtonsClass(theFrame, 3, 1, "8")
i = ButtonsClass(theFrame, 3, 2, "9")
j = ButtonsClass(theFrame, 4, 1, "0")

# Function buttons - equation buttons
k = FuncionalClass(theFrame, 1, 3, "+")
ll = FuncionalClass(theFrame, 2, 3, "-")
m = FuncionalClass(theFrame, 3, 3, "*")
n = FuncionalClass(theFrame, 4, 3, "//")
o = EquationClass(theFrame, 4, 2, "=")
p = DotClass(theFrame, 4, 0, ".")

# Keeps the program running
window.mainloop()
