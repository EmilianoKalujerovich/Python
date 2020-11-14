#Inicializo en vacio, la palabra con mayor cantidad de vocales
#Cantidad de vocales inicia en 0
palabra = ''
vocales = 0

#Ingresar la palabra

pal = input('Ingrese palabra ')

while pal != 'ZZZ':
	#Recorro la palabra en busca de la vocal
	contv = 0
	for letra in pal.lower():
		  if letra in ('a','e','i','o','u'):
					contv = contv + 1
		  #Pregunto si la cantidad de vocales de esa palabra es mayor de la que tenemos guardada
		  if vocales < contv:
			  #Realizo el cambio
			  palabra = pal
			  vocales = contv
			  #Leo la otra palabra
			  pal=input('Ingrese la palabra ')
#Imprimo una de las palabras con mayor cantidad de vocales
print('La palabra con mayor cantidad de vocales es: ', pal)

