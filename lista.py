lista = []
datos = open('datos.csv', 'r')
_ = datos.readline()

for linea in datos.readlines():
    datos_separados = linea.split(";")
    lista.append(datos_separados)

datos.close()

opcion = ""

while opcion != "SALIR":
    print("\n--- MENU ---")
    print("1. Mostrar lista completa")
    print("2. Mostrar lista total/promedio completa")
    print("3. Buscar un año en la lista")
    print("4. Mostrar el total")
    print("5. SALIR")

    opcion = input("\nIngrese una opción: ")

    if opcion == "1":
        for venta in lista:
            print(venta)

    elif opcion == "2":
        suma_total = 0
        contador = 0

        for venta in lista:
            for valor in venta[1:]:
                suma_total += int(valor)
                contador += 1

        promedio = suma_total / contador

        print("Lista total/promedio completa:")
        for venta in lista:
            print(venta)

        print("Suma total: ", suma_total)
        print("Promedio: ", promedio)

    elif opcion == "3":
        anio_buscar = input("Ingrese el año a buscar: ")
        encontrado = False

        for venta in lista:
            if venta[0] == anio_buscar:
                print("Venta encontrada:", venta)
                encontrado = True
                break

        if not encontrado:
            print("No se encontró ninguna venta para el año ingresado.")

    elif opcion == "4":
        suma_total = 0

        for venta in lista:
            for valor in venta[1:]:
                suma_total += int(valor)

        print("Total de ventas:", suma_total)

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
