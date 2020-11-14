suma=0
numeros=int(input("Cuanto numeros va a ingresar?: "))
for f in range(numeros):
    valor=int(input("Ingrese valor:"))
    suma=suma+valor
print("La suma es")
print(suma)
promedio=suma/numeros
print("El promedio es:")
print(promedio)
