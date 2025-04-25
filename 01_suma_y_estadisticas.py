# Bucle que se repite hasta que el usuario ingrese datos válidos
while True:
    try:
        # Solicita al usuario que ingrese números separados por espacio,
        # los divide y los convierte a tipo float
        nums = list(map(float, input("Ingresa los números separados por espacio: ").split()))

        # Imprime la suma de los números
        print(f"Suma: {sum(nums)}")

        # Imprime el número más grande de la lista
        print(f"Máximo: {max(nums)}")

        # Imprime el número más pequeño de la lista
        print(f"Mínimo: {min(nums)}")

        # Finaliza el bucle si todo fue correcto
        break

    # Si ocurre un error al convertir, muestra un mensaje y repite
    except ValueError:
        print("Error: solo números. Intenta de nuevo.")
