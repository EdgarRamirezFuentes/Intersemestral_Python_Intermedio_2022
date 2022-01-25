'''
    Name: 6_tkinter.py
    Description: Use Tkinter to get information from the user
    Author: Edgar Alejandro Ramírez Fuentes
    Date: 01/25/2021
'''
import tkinter as tk
from tkinter import ttk


def show_data():
    '''
        Show the introduced data in a new window
    '''
    # Getting the form data
    global name, age, genre

    # Creating the new window
    new_window = tk.Toplevel(master)
    new_window.title("Show Data")

    # Displaying the information
    ttk.Label(new_window, text="Name: ").grid()
    ttk.Label(new_window, text=name.get()).grid()
    ttk.Label(new_window, text="Age: ").grid()
    ttk.Label(new_window, text=age.get()).grid()
    ttk.Label(new_window, text="Genre: ").grid()
    ttk.Label(new_window, text=genre.get()).grid()
    

# Tkinter app
master = tk.Tk()
master.title('Data form')
main_frame = tk.Frame(master).grid()

# Variables 
name = tk.StringVar()
age = tk.IntVar()
genre = tk.StringVar()

# Inputs and labels
ttk.Label(main_frame, text="Name: ").grid()
ttk.Entry(main_frame, textvariable=name).grid()
ttk.Label(main_frame, text="Age: ").grid()
ttk.Entry(main_frame, textvariable=age).grid()
ttk.Label(main_frame, text="Genre: ").grid()
ttk.Radiobutton(main_frame, text="Male", value="Male", variable=genre).grid(sticky=tk.W)
ttk.Radiobutton(main_frame, text="Female", value="Female", variable=genre).grid(sticky=tk.W)
ttk.Radiobutton(main_frame, text="Other", value="Other", variable=genre).grid(sticky=tk.W)
ttk.Button(main_frame, text="Register", command=show_data).grid()

tk.mainloop()