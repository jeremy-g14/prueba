# haga un programa que si un estudiante saca
# menor a 60 puntos muestre la letra de la nota :
# si el puntaje es menor a 70 ,poner F
# si el puntaje es mayor a 80 ,poner C
# si el puntaje es  ,poner B

puntaje = float(input("escriba la norta :"))
if puntaje >= 91 and puntaje <= 100:
   print("A")
if puntaje >= 81 and puntaje <= 90:
   print("B")
if puntaje >= 71 and puntaje <= 80:
   print("C")
if puntaje >= 61 and puntaje <= 70:
   print("D")
if puntaje >= 51 and puntaje <= 60:
   print("F")
    
