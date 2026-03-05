print("REGISTRO DE NOTAS DE ESTUDIANTES")

cantidad_de_estudiantes = input(f"¿cuantos estudiantes va ingresar?  ")
nombre_del_estudiante = input(f"Ingrese el nombre del estudiante:   ")
total_de_estudiantes = 0
ganan = 0
pierden = 0
suma_de_promedios = 0

while True:
    print("ingrese notas")
    nota1 = float(input(f"Ingrese la primera nota del estudiante: "))
    nota2 = float(input(f"Ingrese segunda nota del estudiante:  "))
    nota3 = float(input(f"Ingrese la tercera nota del estudiante: "))

    promedio_del_estudiante = (nota1 + nota2 +nota3) / 3 
    print(f"el promedio del estudiante es: {promedio_del_estudiante}")
    
    total_de_estudiantes += 1
    suma_de_promedios += 1

    if promedio_del_estudiante >= 3:
        print("felicitaciones gano el estudiante") 
        ganan += 1
    else: 
        print("reprobo el estudiante")
        pierden += 1 

    if promedio_del_estudiante > 6:
        print("error en las notas el mayor promedio es 5.0")

    promedio_general_del_curso = suma_de_promedios / total_de_estudiantes
    print(f"total de estudiantes:", total_de_estudiantes)
    print(f"Estudiantes que ganan:", ganan)
    print(f"estudiantes que pierden:", pierden)
    print(f"Promedio general:", suma_de_promedios)

    opcion = input("¿desea registrar otro alumno si/no?"  )
    if opcion.lower() == "no":
        print("programa finalizado")
        break 
