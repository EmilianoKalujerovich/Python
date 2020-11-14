sexo=input("Ingrese sexo: ")
altura=int(input("Ingrese altura: "))

if sexo == 'femenino' and altura < 145:
    print("Es una persona petisa")
if sexo == 'femenino' and altura > 145 and altura < 170:
    print("Es una persona normal")
if sexo == 'femenino' and altura > 170:
    print("Es una persona alta")
if sexo == 'masculino' and altura < 160:
    print("Es una persona petisa")
if sexo == 'masculino' and altura > 160 and altura < 190:
    print("Es una persona normal")
if sexo == 'masculino' and altura > 190:
    print("Es una persona alta")



