# Intenta pedir al usuario números separados por espacio y sumar
try:
    # Pide al usuario una línea de entrada, la divide por espacios
    # y convierte cada parte en número flotante
    numeros = list(map(float, input("Ingresa los números separados por espacio: ").split()))
    
    # Calcula e imprime la suma de todos los números ingresados
    print(f"Suma: {sum(numeros)}")

# Si el usuario ingresa algo que no sea número, muestra error
except ValueError:
    print("Error: solo se permiten números reales separados por espacio.")