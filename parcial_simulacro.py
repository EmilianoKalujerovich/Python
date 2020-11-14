#Creo una funcion sin ningun parametro para el ingreso de informacion.
def cargarProductos():
	#Ingreso la primera pregunta y debajo una lista vacia donde se guardara esa informacion
 marca = input("ingrese el nombre del producto: ")
 lista = []
 #Como hay una condicion, creo un ciclo while que se detendra cuando != 'zzz'
 while marca != "zzz":
	 #Sigo guardando informacions
  tipo = input("ingrese el tipo  de producto: ")
  monto = float(input("ingrese el precio del producto: "))
  cantidad = int(input("ingrese la cantidad compra: "))
  #Guardo la informacion en la lista con un 'append'
  lista.append([marca,tipo,monto, cantidad])
  #Sigo preguntando para que vuelva a iniciar el ciclo
  marca = input("ingrese el nombre del producto: ")
  #Retorno la lista con la informacion ingresada
 return lista
	

def calcularMonto (l):
 montoacumulado = 0
 for producto in l:
  if producto[0]=="alba":
   montoacumulado = montoacumulado +   producto[2] * producto[3]	
 print ("El monto vendio de Alba es de " , montoacumulado)	
	 	
	#
productos = cargarProductos()
calcularMonto(productos)
