import tkinter as tk
from tkinter import ttk

#creamos la ventana con valores por defecto
root = tk.Tk() 
etiqueta = tk.Label(root, text="Bienvenidos")
etiqueta.grid(row=0,column=0) #muestra en la panntalla

marco_principal = tk.Frame() #define un marco
marco_principal.grid() #muestra el marco
marco_principal.config(width="800", height="600", bg="red")

boton1 = tk.Button(root,text="no presiones el botón", width="30", height="10").grid(row=0, column=2)

root.mainloop()  #hace que se refresque la ventana en bucle