#Magic 8 ball
import random
import tkinter
from tkinter import ttk #For themed widgets

responses = ['si','no','eres tu','te odia','preub de nuevo','estas solo','mala suerte','preuabas de nuevo','gracias','intentalo otra vez','bienvenido','oahio','sumimasen','adios','guay','ultimo','pregunta de nuevo']

question = ''

while question != 'q':
 
 question = input("Introduce a question: ")
 print("Thinking..")
 print(random.choice(responses))
 question = input("Quieres haces otra pregunta?: \nPulsa 'q' para salir. ")
 if question == 'q':
  break
 else:
  print(random.choice(responses))

