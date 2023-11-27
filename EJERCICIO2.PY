clase  = {}
while True:
    decision = input("Qué deseas hacer? (1) Añadir alumno/a, (2) Mostrar " 
                 "número de aprobados, (3) Mostrar todo el alumnado. "
                 "Ingresa el número de la opción: ")
    if decision == "1":
        alumno = input("Indica el nombre del alumno y si está aprobado(1) ó "
                   "suspendido(0) siguiendo el siguiente formato: "
                   "(NOMBRE 1): ")
        nombre, nota = alumno.split()
        if nota == "1":
            nota = True
        else:
            nota = False
        clase[nombre] = nota
        print (clase)
    if decision == "2":
        aprobados = 0
        print ("El numero de aprobados es: ", aprobados)
    if decision == "3":
        print (clase.keys())
