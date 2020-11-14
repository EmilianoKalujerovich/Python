def cargarInfoPaquetes():

    listaPaquetes=[]

    for i in range(20):   
        print("Paquete " + str(i+1) + " de 20")#Paquete 1 de 20
        destino = input("ingresar el destino ")
        comprador = input("ingresar el nombre del comprador: ")
        fecha = input("ingresar la fecha de partida ")
        costoDia = float(input("ingresar el costo diario: "))
        hotel = input("ingresar el hotel: ")
        aerolínea = input("ingresar aerolínea: ")
        dias = int(input("ingresar la cantidad de dias: "))
        costoArealinea =  float(input("ingresar el costo de la areolinea: "))
        listaPaquetes.append([destino, comprador, fecha, costoDia, hotel, aerolínea, dias, costoArealinea ])
    return listaPaquetes

def imprimirCostos(paquetes):
#[destino, comprador, fecha, costoDia, hotel, aerolínea, dias, costoArealinea ]
    for paquete in paquetes:
       comprador = paquete[1]
       aerolinea = paquete[5]            
       costoEstadia = paquete[3]*paquete[6]
       costoAerolinea = paquete[7]

       if aerolinea != "Aerolíneas Argentinas":  
           costoTotal = costoEstadia + costoAerolinea  
           print("El costo total del comprador " + comprador + "es " + str(costoTotal))         
       else:
           costoTotal = costoEstadia - costoEstadia*0.15 + costoAerolinea
           print("El costo total (con descuentos) del comprador " + comprador + "es " + str(costoTotal)) 

            
paquetes = cargarInfoPaquetes()
imprimirCostos(paquetes)


