

nombres = []
for x in range(1,3):
	nombres.append(input("Escribe un nombre: ").lower())

cantidad = 0

for nombre in nombres:
	for letra in nombre:
		if letra == 'a':
			cantidad = cantidad + 1
			break
		else:
			cantidad = cantidad
print(cantidad)
    
