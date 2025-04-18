numeros = input("Ingresa los números separados por espacio: ")

# Convertir la entrada en una lista de números flotantes
lista = list(map(float, numeros.split()))

# Calcular y mostrar la suma
print("La suma es:", sum(lista))