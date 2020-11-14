#Creo las listas

listaMujeres=[]
listaVarones=[]

#Leo datos ingresados hasta que nombre sea diferente a 'AAA'

nombre = input('Ingrese un nombre')
while nombre != 'AAA':
			sexo = input('Ingrese el sexo. Si es femenino es F. Si es masculino es M ') 
	#Controlo que el sexo ingresado sea valido
			while sexo != 'F' and sexo != 'M':
					print('El caracter ingresado no pertenece a ningun sexo')
					sexo = input('Ingrese el sexo. Si es femenino es F. Si es masculino es M') 
			if sexo == 'F':
				listaMujeres.append(nombre)
			else:
	    
				listaVarones.append(nombre)
	        
			nombre = input('Ingrese un nombre')
	
print('La lista de mujeres es: ')
#Recorro e imprimo la lista de mujeres..
cont=0
while cont < len(listaMujeres):
	print(listaMujeres[cont])
	cont = cont + 1
print('La lista de hombres es: ')
#Recorro e imprimo la lista de mujeres..
cont=0
while cont < len(listaVarones):
	print(listaVarones[cont])
	cont = cont + 1
	
