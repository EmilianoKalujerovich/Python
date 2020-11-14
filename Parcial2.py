def ingresarDatosAlumnos():

    listaAlumnos =[]
    nombre = input("Ingresar el nombre: ")

    while nombre != "zzz":
        apellido = input("Ingresar apellido: ")
        email = input("Ingresar email: ")
        nota = int(input("Ingresar Nota: "))
        listaAlumnos.append([nombre, apellido, email, nota])
        nombre = input("Ingresar el nombre: ")
        
    return listaAlumnos

def reporteNotas(listaAlumnos):
    listaAprobados = []
    listaReprobados = []
    cantAprobados = 0
    sumaNotas = 0

    for alumno in listaAlumnos: 
        nota = alumno[3]
        if nota >= 4:
            listaAprobados.append([alumno[0], alumno[1]])
            cantAprobados = cantAprobados + 1
        else:
            listaReprobados.append([alumno[0], alumno[1]])  
        sumaNotas = sumaNotas + nota      
        
    porcentajeAprobados = cantAprobados*100 / len(listaAlumnos)
    promedioNotas = sumaNotas/len(listaAlumnos)
    print("Lista de aprobados: " + str(listaAprobados))
    print("Lista de reprobados: " + str(listaReprobados))
    
    print("El porcentaje de aprobados es: " + str(porcentajeAprobados))
    print("El promedio de notas es: " + str(promedioNotas))


def imprimirPeorYMejor(listaAlumnos):

    mejorAlumno = listaAlumnos[0]
    peorAlumno = listaAlumnos[0] 
else:
            listaVeganos.append([producto[0], producto[4]])
    for alumno in listaAlumnos:
        nota = alumno[3]
        if nota > mejorAlumno[3]:
            mejorAlumno = alumno
        
        if nota < peorAlumno[3]:
            peorAlumno = alumno 
   
    print("El peor alumno es: " + peorAlumno[0] + ", " + peorAlumno[1] + ". Nota: " + str(peorAlumno[3]) )
    print("El mejor alumno es: " + mejorAlumno[0] + ", " + mejorAlumno[1] + ". Nota: " + str(mejorAlumno[3]) )

def imprimirEstadoAlumno(listaAlumnos):
    nombre = input("Ingrese el nombre de un alumno: ")
    apellido = input("Ingrese el apellido de un alumno: ")
    resultado = "El alumno que ingreso no esta en la lista"
    
    for alumno in listaAlumnos:
        if nombre == alumno[0] and apellido == alumno[1]:
            if alumno[3] >= 4: 
                resultado = nombre + ", " + apellido + " Aprobó"
            else:
                resultado = nombre + ", " + apellido + " Reprobó"
            break
    
    print(resultado)


listaAlumnos = ingresarDatosAlumnos()
reporteNotas(listaAlumnos)
imprimirPeorYMejor(listaAlumnos)
imprimirEstadoAlumno(listaAlumnos)
