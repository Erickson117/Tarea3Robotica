#Alumno: Reyes Garcia Erick Jesus
#Grupo: 1058
#Asignatura: Robotica.

import math
#math.degrees()

def calcularXY(theta1,theta2):
  #Longitudes de ambos ejes
  l1 = 1.3
  l2 = 0.8
  #Calcular X y Y
  x = (l1*math.cos(math.radians(theta1))) + (l2*math.cos(math.radians(theta1 + theta2)))
  y = (l1*math.sin(math.radians(theta1))) + (l2*math.sin(math.radians(theta1 + theta2)))
  return f"({x},{y})" #valor a regresar

#Ingresar los angulos desde el teclado y comprobando que se metan numeros
error = 0 #esta variable la uso para evitar que se impriman las coordenadas con los datos en memoria cuando se introducen caracteres invalidos

try:
  theta1 = int(input("Ingresa tu valor de theta1: "))
  theta2 = int(input("Ingresa tu valor de theta2: "))
except:
  print("Estas introduciendo valores no validos")
  error += 1


#comprobar que solo se muevan en el rango permitido en este caso el primero va de 0 a 180 y el segundo de 0 a 90
if(theta1 < 0 or theta1 > 180 ):
  print("Valores no validos para theta 1")
elif(theta2 < 0 or theta2 > 90):
  print("Valores no validos para theta 2")
elif(error == 0):
  print("Las coordenadas del efector final se encuentran en: "+calcularXY(theta1,theta2)) #Imprime el resultado
