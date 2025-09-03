from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hola Soy Gonzalo y este es mi primer programa UI").grid(column=4, row=4)
ttk.Button(frm, text="MI primer boton", command=root.destroy).grid(column=1, row=0)
root.mainloop()