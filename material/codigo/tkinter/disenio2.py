from ast import Lambda
from cgitb import text
from tkinter import Tk, mainloop
from tkinter import ttk
from tkinter import *
from turtle import width

def show_name(name):
    name_label.set(name.get())

main = Tk()
main.title("App 1")

main_frame = ttk.Frame(main, padding="50").grid(column=0, row=0, sticky=(W,E,S,N))

username = StringVar()

ttk.Entry(main_frame, width=10, textvariable=username).grid(column=0, row=1)
ttk.Label(main_frame, text="Introduce tu nombre en el campo: ").grid(column=0, row=0, columnspan=2)
ttk.Button(main_frame, text="Registrar!", command=lambda: show_name(username)).grid(column=0, row=2)


name_label = StringVar()
ttk.Label(main_frame, text="Your name is:").grid(column=0, row=3)

ttk.Label(main_frame, textvariable=name_label).grid(column=0, row=4)
mainloop()
