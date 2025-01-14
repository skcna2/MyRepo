#Magic 8 ball
import random

question = input("Introduce a question: ")
print("Thinking..")

responses = ['si','no','eres tu','te odia','preub de nuevo','estas solo','mala suerte','preuabas de nuevo','gracias','intentalo otra vez','bienvenido','oahio','sumimasen','adios','guay','ultimo','pregunta de nuevo']

print(random.choice(responses))