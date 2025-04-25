numeros = input("Ingresa los numeros a evaluar (separados por un espacio):")
lista = list(map(float, numeros.split()))
print(f"El numero mas grande es {max(lista)}")