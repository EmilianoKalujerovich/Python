def guardarInformacion():
	
	marca = input ('Ingrese marca: ')
	listaPintura=[]
	while marca != "zzz":
		
		tipo_producto = input('Ingrese tipo de producto: ')
		monto = float(input('Ingrese monto: '))
		cantidad = int(input('Ingrese cantidad: '))
		listaPintura.append([marca, tipo_producto,monto,cantidad])
		
		marca = input ('Ingrese marca: ')
		
		return listaPintura

def imprimirCosto(l):
	montoAcumulado = 0
	for pintura in l:
		if pintura[0] == "alba":
			montoAcumulado = montoAcumulado +  pintura[2] * pintura[3]
	print("El costo final es de: ", montoAcumulado)
	
pintura = guardarInformacion()
imprimirCosto = (pintura)

	
