def mostrar_parqueadero():
    print(parqueadero)

espacios = 10
opcion = 1
parqueadero = ["vacio"]* espacios

while opcion < 4:
    opcion = int(input(" escoge opcion : 1.ingresar , 2. retirar , 3.mostrar parqueadero , 4.salir"))

    if opcion == 1:
        if "vacio" in parqueadero:
            placa = input("ingresa la placa:  ").upper()
            if placa in parqueadero:
                print("carro ingresado")
            else: 
                index = parqueadero.index("vacio")
                parqueadero[index] = placa
            
        else:
            print("parqueadero lleno")
            
        mostrar_parqueadero()
    elif opcion == 2:
        if parqueadero.count("VACIO") != 10:
            placa = input("ingrese la placa a retirar")
            if placa in parqueadero:
                index = parqueadero.index(placa)
                parqueadero[index] = "vacio"
            else:
                print("el carro no esta ingresado ")
        else:
            print("parqueadero esta vacio")
        mostrar_parqueadero()
    elif opcion == 3:
        mostrar_parqueadero()

with open("carrosdentro.txt", "w")as archivo:
    archivo.write(str(parqueadero))


