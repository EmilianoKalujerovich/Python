def dietetica():

    listaProductos =[]
    
    nombre = input("Ingresar el nombre: ")

    while nombre != "pancho":
        apto_celiaco = input("Ingresar si es apto para celiacos: ")
        apto_vegano = input("Ingresar si es apto para veganos: ")
        calorias = input("Ingresar calorias: ")
        precio = int(input("Ingresar precio: "))
        listaProductos.append([nombre, apto_celiaco, apto_vegano, calorias,precio])
        nombre = input("Ingresar el nombre: ")
        
    return listaProductos
    
    
def listasFinales(listaProductos):
    listaVeganos = []
    listaCeliacos = []
    
    for producto in listaProductos: 
        celiaco = producto[1]
        vegano = producto[2]
        costo = producto[4]
        porcentaje = 0
        if celiaco == "si" and costo < 35:
            listaCeliacos.append([producto[0], producto[4]])
            porcentaje = porcentaje + 1
        if vegano == "si":
            listaVeganos.append([producto[0], producto[4]]) 
            
    porcentajeFinal = porcentaje*100 / len(listaProductos)         
    print("Lista de celiacos es: " + str(listaCeliacos))
    print("Lista de veganos es: " + str(listaVeganos))
    print("El porcentaje de celiacos es de: " + str(porcentajeFinal))
    
    
    
productos =dietetica()
listasFinales(productos)

