# login.py

# list of imported packages
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog
import os

# creates the login screen
root = Tk()
root.title("Log In")
root.minsize(width=300, height=150)
root.maxsize(width=300, height=150)

# progress bar widget
progress = Progressbar(root, orient = HORIZONTAL, 
              length = 100, mode = 'determinate') 

# command for button1
def run1():
    os.startfile(r"file location for button 1")

# command for button2
def run2():
    os.startfile(r"file location for button 2")

# command for button 3
def run3():
    os.startfile(r"file location for button 3")

# command for button 4
def run4():
    os.startfile(r"file location for button 4")

# checks if he password is correct
def check_pass():
    if pass_enter.get() == "Admin":
        correct()
    else:
        incorrect()

# displays correct if the entered password is correct
def correct():
    pass_correct = Label(root, text="Password Correct!")
    pass_correct.pack()
    progress.pack(pady = 10)
    bar()

# displays incorrect if the entered password is wrong
def incorrect():
    pass_incorrect = Label(root, text="Password Incorrect!")
    pass_incorrect.pack()

# creates a window to ask the user where they want to go
def create_window():
    global welcome
    top = Toplevel()
    top.title("Programs")
    top.minsize(width=300, height=150)
    top.maxsize(width=300, height=150)
    welcome = Label(top, text="Welcome User!").pack()
    choose = Label(top, text="Where do you want to go?").pack()
    button1 = Button(top, text="Button 1", command=run1)
    button2 = Button(top, text="Button 2", command=run2)
    button3 = Button(top, text="Button 3", command=run3)
    button4 = Button(top, text="button 4", command=run4)
    
    # packing the buttons onto the screen
    button1.pack(padx=20)
    button2.pack(padx=20)
    button3.pack(padx=20)
    button4.pack(padx=20)

# creates a loading bar when the password is correct
def bar(): 
    import time 
    progress['value'] = 25
    root.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 50
    root.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 75
    root.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 100
    root.update_idletasks() 
    time.sleep(1) 
    create_window()

# defining widjets for login screen
label1 = Label(root, text="Hello, User!")
label2 = Label(root, text="Program HUB")
pass_enter = Entry(root, width=20, show="*")
button1 = Button(root, text="Log In", command=check_pass)

# placing widgets for login screen
label1.pack()
label2.pack()
pass_enter.pack()
button1.pack()


root.mainloop()
