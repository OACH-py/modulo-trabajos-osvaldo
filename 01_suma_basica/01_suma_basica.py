# Inicia un ciclo infinito que se repetirá hasta que el usuario ingrese una entrada válida
while True:
    # Solicita al usuario que ingrese números separados por espacios
    numeros = input("Ingresa los números separados por espacio: ")
    
    try:
        # Intenta dividir la cadena en partes y convertir cada una a float
        # Esto puede fallar si algún valor no es un número válido
        lista = list(map(float, numeros.split()))
        
        # Si la conversión fue exitosa, calcula la suma de los números
        print(f"La suma es:{sum(lista)}")
        
        # Sale del ciclo porque la entrada fue válida
        break

    # Si ocurre un error al convertir a float (por ejemplo, si se escribe "abc"), entra aquí
    except ValueError:
        # Muestra un mensaje de error indicando que la entrada no fue válida
        print("Error: Solo se permiten números. Intenta de nuevo.")