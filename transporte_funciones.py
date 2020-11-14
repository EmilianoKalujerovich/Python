import math

def calculo_transporte(x,y,b,c,d):
	if d > x and d >y and d > b and d > c :
    return d
x = input(("Ingrese cantidad de alumnos de 1era: "))
y = input(("Ingrese cantidad de alumnos de 2da: "))
b = input(("Ingrese cantidad de alumnos de 3ra: "))
c = input(("Ingrese cantidad de alumnos de jardin: "))
d = 35

print("La cantidad de alumnos son: " , calculo_transporte(d))



