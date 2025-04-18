# Inicia un ciclo infinito que se repetirá hasta que el usuario ingrese una entrada válida
while True:

    # Solicita al usuario que ingrese números separados por espacios
    numeros = input("Ingresa los números separados por espacio: ")

    try:
        # Divide la entrada por espacios y convierte cada elemento a tipo float
        lista = list(map(float, numeros.split()))

        # Calcula la suma de los números
        print(f"La suma es: {sum(lista)}")

        # Encuentra y muestra el número más grande
        print(f"El número más grande es: {max(lista)}")

        # Encuentra y muestra el número más pequeño
        print(f"El número más pequeño es: {min(lista)}")

        # Calcula el promedio: suma total entre cantidad de elementos
        promedio = sum(lista) / len(lista)
        print(f"El promedio es: {promedio}")

        # Si todo fue correcto, rompe el ciclo y termina
        break

    # Captura errores si el usuario ingresó un dato no numérico
    except ValueError:
        print("Error: Solo se permiten números. Intenta de nuevo.")