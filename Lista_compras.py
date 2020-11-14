prod=input('Ingrese primer producto: ')
cant=input('Ingrese cantidad: ')
precio=input('Ingrese precio: ')
total= int(precio)* int(cant)



prod_uno=input('Ingrese segundo producto: ')
cant_uno=input('Ingrese cantidad: ')
prec_uno=input('Ingrese precio: ')
total_uno= int(prec_uno)* int(cant_uno)


prod_dos=input('Ingrese tercer producto: ')
cant_dos=input('Ingrese cantidad: ')
prec_dos=input('Ingrese precio: ')
total_dos= int(prec_dos)* int(cant_dos)

prod_tres=input('Ingrese cuarto producto: ')
cant_tres=input('Ingrese cantidad: ')
prec_tres=input('Ingrese precio: ')
total_tres= int(prec_tres)* int(cant_tres)

total_todo= int(precio) * int(cant) + int(prec_uno) * int(cant_uno) + int(prec_dos) * int(cant_dos) + int(prec_tres) * int(cant_dos) + int(prec_tres) * int(cant_tres)

print('Usted eligio el producto: ' + prod + ' con la cantidad de: '+ str(cant) + '. Precio final es de : ' + str(total))
print('Usted eligio el producto: ' + prod_uno + ' con la cantidad de: ' + str(cant_uno) + '. Precio final es de : ' + str(total_uno))
print('Usted eligio el producto: ' + prod_dos + ' con la cantidad de: ' +  str(cant_dos) + '. Precio final es de : ' +str(total_dos))
print('Usted eligio el producto: ' + prod_tres+ ' con la cantidad de: ' + str(cant_tres) + '. Precio final es de : ' +str(total_tres))
print('El total de su compra es de: ' + str(total_todo))




