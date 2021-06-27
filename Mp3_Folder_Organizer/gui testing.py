# Imports tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

# toplevel window
root = Tk()


# method to make widget invisible
# or remove from toplevel
def forget(widget):
    # This will remove the widget from toplevel
    # basically widget do not get deleted
    # it just becomes invisible and loses its position
    # and can be retrieve
    widget.grid_forget()


# method to make widget visible
def retrieve(widget):
    widget.grid(row=0, column=0, ipady=10, pady=10, padx=5)


# Button widgets
b1 = Button(root, text="Btn 1")
b1.grid(row=0, column=0, ipady=10, pady=10, padx=5)

# See, in command forget() method is passed
b2 = Button(root, text="Btn 2", command=lambda: forget(b1))
b2.grid(row=0, column=1, ipady=10, pady=10, padx=5)

# In command retrieve() method is passed
b3 = Button(root, text="Btn 3", command=lambda: retrieve(b1))
b3.grid(row=0, column=2, ipady=10, pady=10, padx=5)

# infinite loop, interrupted by keyboard or mouse
mainloop()
