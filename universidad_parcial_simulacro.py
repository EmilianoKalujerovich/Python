def parciales():
	#Ingreso la primera pregunta y debajo una lista vacia donde se guardara esa informacion
 nombre = input("ingrese nombre: ")
 lista = []
 #Como hay una condicion, creo un ciclo while que se detendra cuando != 'zzz'
 while nombre != "zzz":
	 #Sigo guardando informacions
  apellido = input("ingrese apellido: ")
  email = input("ingrese email: ")
  nota = int(input("ingrese nota: "))
  #Guardo la informacion en la lista con un 'append'
  lista.append([nombre,apellido,email, nota])
  #Sigo preguntando para que vuelva a iniciar el ciclo
  nombre = input("ingrese el nombre: ")
  #Retorno la lista con la informacion ingresada
 return lista

def calcularAprobados (A):
 for aprobados in A:
	 if aprobados[3] >= 4:
		 print("El alumno", aprobados[0],"aprobo")
		 	
def calcularDesaprobados (D):
 for desaprobados in D:
	 if desaprobados[3] < 4:
		 print("El alumno", desaprobados[0],"desaprobo")

def porcentaje (P):
	total= 0
	for porcentaje in P:
		total = porcentaje [3] * porcentaje [3] / 100
		print("El porcentaje de aprobados es: ", total)
	 
	 

	
	
universidad= parciales()
calcularAprobados(universidad)
calcularDesaprobados(universidad) 
porcentaje(universidad) 
