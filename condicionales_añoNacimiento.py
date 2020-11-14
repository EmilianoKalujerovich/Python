añoNacimiento=int(input("Ingrese año de nacimiento: "))


if añoNacimiento < 2:
    print("Es un bebé")
elif añoNacimiento >= 2 and añoNacimiento <= 12 :
	print("Es un menor")
elif añoNacimiento > 12 and añoNacimiento <= 18 :
	print("Es un adolescente")
elif añoNacimiento > 18 and añoNacimiento <= 45 :
	print("Es un adulto")
elif añoNacimiento > 45 and añoNacimiento <= 60 :
	print("Es un veterano")
elif añoNacimiento > 60 :
	print("Es un abuelo")


