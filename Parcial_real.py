def consumo_gas():

    lista_clientes =[]
    for i in range(20):	
    dni = input("Ingresar el dni: ")
    consumo = float(input("Ingresar consumo "))
    monto = float(input("Ingresar monto "))
    localidad = input("Ingresar localidad ")
    
    lista_clientes.append([dni, consumo, monto, localidad])
    return lista_clientes
    
    
def consumo_clientes(consumo):
	
    lista_consumo = []
    lista_monto = []
    
    for consumos in consumo: 
        dni = consumos[0]
        consumo = consumos[1]
        monto = consumos[2]
        localidad = consumos[3]
        
        if consumo > 300:
            lista_consumo.append([dni, consumo])
        if monto > 500 and localidad == "capital federal":
            lista_monto.append([dni]) 
            
            
            print("el dni: " + dni + "supero el consumo de 300 con" + str(consumo))
            print("el dni: " + dni)
            

   
consumo =consumo_gas()
consumo_clientes(consumo)
