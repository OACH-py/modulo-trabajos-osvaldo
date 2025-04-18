# Solicita al usuario que ingrese números separados por espacios
numeros = input("Ingresa los números separados por espacio: ")

# Divide la cadena ingresada en una lista de cadenas y convierte cada elemento a flotante
lista = list(map(float, numeros.split()))

# Calcula la suma de los elementos de la lista
print("La suma es:", sum(lista))