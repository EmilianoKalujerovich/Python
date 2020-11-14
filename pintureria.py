lista_pinturas=[]


tipo_producto = input(("Ingrese el tipo de pintura: "))
marca = input(("Ingrese la marca: "))
monto = input(("Ingrese el monto: "))
cantidad = input(("Ingrese cantidad: "))
	


while tipo_producto != 'ZZZ':
	lista_pinturas.append(marca  + tipo_producto +  monto + cantidad )
	
    
    
	tipo_producto = input(("Ingrese el tipo de pintura: "))
	marca = input(("Ingrese la marca: "))
	monto = input(("Ingrese el monto: "))
	cantidad = input(("Ingrese cantidad: "))
	
print('La lista de pinturas es: ')
cont=0
while cont < len(lista_pinturas):
	print(lista_pinturas[cont])
	cont = cont + 1




