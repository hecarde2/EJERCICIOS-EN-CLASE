espacios = 10
carros_dentro = 5
while True: 
    print(f"carros actualmente adentro {carros_dentro}")
    print("1. ingresar carro")
    print("2. sacar carro")
    print("3. salir de sistema")
    
    opcion = input("selecione una opcion")

    if opcion == "1":
        if carros_dentro < espacios:
            carros_dentro += 1
            print("ingreso vehiculo")
        else:
            print("no hay espacios disponibles")

    if opcion == "2":
        if carros_dentro > 0:
          carros_dentro -= 1
          print("salio vehiculo")
        else:
            print("espacios vacios para parquear")
    
    if opcion == "3":
       print("saliendo del sistema")
       break
       
 

