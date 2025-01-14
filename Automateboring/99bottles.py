"""99 botellas
Cree un programa que imprima cada línea de la canción "99 botellas de cerveza en la pared".
-No utilice una lista para todos los números y no los escriba todos manualmente. 
Utilice una función integrada en su lugar.
-Además de la frase "Take one down", no puedes escribir ningún número o 
nombre de número directamente en la letra de tu canción.
-Recuerde, cuando llegue a 1 botella restante, la palabra "botellas" se vuelve singular.
FRASEEJEMPLO:23 bottles of beer on the wall, 23 bottles of beer.
Take one down and pass it around, 22 bottles of beer on the wall."""

frase = "99 bottles of beer on the wall, 99 bottles of beer.\nTake one down and pass it around, 98 bottles of beer on the wall."

for i in reversed(range(1,100)): #podría ser también  for i in range(99,0,-1):
    i2 = i-1
    if i>=2:
     
     print(f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down and pass it around,{i2} bottles of beer on the wall.")
    elif i<2:
     
     print(f"{i} bottle of beer on the wall, {i} bottle of beer.\nTake one down and pass it around,no more bottles of beer on the wall.")
     
print("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")