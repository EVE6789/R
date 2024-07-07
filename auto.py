vehiculos = []
duenos = []

while True:
    print("\nMenú:")
    print("1. Agregar vehículo")
    print("2. Agregar dueño")
    print("3. Mostrar datos")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        marca = input("Ingrese la marca del vehículo: ")
        modelo = input("Ingrese el modelo del vehículo: ")
        while len(marca) < 3 or len(modelo) < 3:
            print("La marca y el modelo deben tener al menos 3 letras.")
            marca = input("Ingrese la marca del vehículo: ")
            modelo = input("Ingrese el modelo del vehículo: ")

        precio = float(input("Ingrese el precio del vehículo: "))
        while precio < 5000000:
            print("El precio debe ser al menos 5.000.000.")
            precio = float(input("Ingrese el precio del vehículo: "))

        if precio > 20000000:
            precio += precio * 0.10

        vehiculos.append({"Marca": marca, "Modelo": modelo, "Precio": precio})
    elif opcion == "2":
        nombre = input("Ingrese el nombre del dueño: ")
        while len(nombre) < 3:
            print("El nombre debe tener al menos 3 letras.")
            nombre = input("Ingrese el nombre del dueño: ")

        edad = int(input("Ingrese la edad del dueño: "))
        while edad < 18:
            print("El dueño debe ser mayor de edad.")
            edad = int(input("Ingrese la edad del dueño: "))

        rut = int(input("Ingrese el RUT del dueño: "))
        while rut < 5000000 or rut > 28000000:
            print("El RUT debe estar entre 5.000.000 y 28.000.000.")
            rut = int(input("Ingrese el RUT del dueño: "))

        duenos.append({"Nombre": nombre, "Edad": edad, "RUT": rut})
    elif opcion == "3":
        print("Vehículos:")
        for vehiculo in vehiculos:
            print(vehiculo)
        print("Dueños:")
        for dueno in duenos:
            print(dueno)
    elif opcion == "4":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
