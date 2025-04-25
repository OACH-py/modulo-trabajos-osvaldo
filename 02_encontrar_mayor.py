# Solicita al usuario que ingrese números separados por espacios
entrada = input("Ingresa los números a evaluar (separados por un espacio): ")

# Convierte la cadena de entrada en una lista de números flotantes
numeros = list(map(float, entrada.split()))

# Imprime el número más grande de la lista
print(f"El número más grande es {max(numeros)}")