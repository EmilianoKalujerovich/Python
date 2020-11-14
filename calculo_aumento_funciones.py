import math

def calculo_nuevo_precio(x,y):
    return x * y / 100 + x
    
    
x = float(input("Ingrese el precio anterior: "))
y=  float(input("Ingrese el porcentaje a aumentar: "))


print("El precio aumentado es de: ", calculo_nuevo_precio(x,y))
