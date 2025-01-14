import tkinter as tk
from tkinter import ttk

def enter_data():
    nombre = first_name_entry.get()
    

window = tk.Tk()
window.title("Data Entry Form")

frame = tk.Frame(window)  #this frame is contained inside the window i have created
frame.pack()

#saving user info. PRIMER CUADRO
user_info_frame = tk.LabelFrame(frame, text="user Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

#saving user registration
user_reg_frame = tk.LabelFrame(frame)
user_reg_frame.grid(row=1, column=0, sticky= "news" ,padx=20, pady=10)

#Frame terms and conditions
user_terms_frame = tk.LabelFrame(frame, text ="Terms & conditions")
user_terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

#Frame boton guardar
button = tk.Button(frame, text="Enter Data")
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

#PRIMER CUADRO
#etiquetas primer cuadro

first_name_label = tk.Label(user_info_frame, text="Firt Name")
first_name_label.grid(row=0, column=0)
last_name_label = tk.Label(user_info_frame,text= "Last Name")
last_name_label.grid(row=0,column=1)

#Cuadros de texto primer cuadro
first_name_entry = tk.Entry(user_info_frame)
last_name_entry = tk.Entry(user_info_frame)

first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

#combobox

title_label = tk.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

#spinbox
title_spin =  tk.Label(user_info_frame, text="Age")
spin_age = ttk.Spinbox(user_info_frame, from_=18, to=110)
title_spin.grid(row=2, column=0)
spin_age.grid(row=3, column=0)

#combobox nacionalidad
natio_title = tk.Label(user_info_frame, text="Nacionality")
natio_combobox = ttk.Combobox(user_info_frame,values=["España","Angola","Filipinas","Francia"])
natio_title.grid(row=2,column=1)
natio_combobox.grid(row=3, column=1)

#SEGUNDO CUADRO
#Registration Status

reg_status_title = tk.Label(user_reg_frame, text="Registration status")
reg_status_check = tk.Checkbutton(user_reg_frame, text="Currently Registered")
reg_status_title.grid(row=0 ,column=0)
reg_status_check.grid(row=1, column=0)

reg_completed = tk.Label(user_reg_frame, text="#Completed Courses")
reg_spin = ttk.Spinbox(user_reg_frame, from_=0, to= 10)
reg_completed.grid(row=0, column=1)
reg_spin.grid(row=1, column=1)

reg_sem = tk.Label(user_reg_frame, text="#Semesters")
reg_spin_sem = ttk.Spinbox(user_reg_frame, from_=0, to= 10)
reg_sem.grid(row=0, column=2)
reg_spin_sem.grid(row=1, column=2)

#TERCER CUADRO

terms_check = tk.Checkbutton(user_terms_frame,command=enter_data, text="I accept the terms and conditions")
terms_check.grid(row=0, column=0)

#Config de los grids que heredan de user_info_frame

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#Config de los grids que heredan de reg_info_frame

for widget in user_reg_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


window.mainloop()