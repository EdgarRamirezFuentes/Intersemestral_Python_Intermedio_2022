from tkinter import * # Llamadas de módulos de tkinter
from tkinter import ttk # Trabaja con nuevos módulos de tkinter

main = Tk() # Creando un fram de tkinter

# Main frame
main_frame = ttk.Frame(main, padding="25 50").grid(column=0, row=0, sticky=(N,W,E,S))

# Botones
ttk.Button(main_frame, text="Boton nuevo").grid(column=0, row=1, sticky=W)

# Labels
ttk.Label(main_frame, text="Hola mundo").grid(column=0, row=0)
ttk.Label(main_frame, text="Otro label").grid(column=1, row=0)

# Entry
ttk.Entry(main_frame, width=8).grid()

# Radiobutton
rb1 = ttk.Radiobutton(main_frame, text="M", value="M").grid(sticky=W)
rb2 = ttk.Radiobutton(main_frame, text="F", value="F").grid(sticky=W)

# Frame

main.mainloop()


