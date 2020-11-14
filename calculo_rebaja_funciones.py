import math

def calculo_rebaja(x,y):
    return x * y / 100
    
    
x = float(input("Ingrese el precio: "))
y=  float(input("Ingrese el descuento: "))


print("El porcentaje de la rebaja es: ", calculo_rebaja(x,y))




