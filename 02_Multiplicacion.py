import math

numeros = list(map(float, input("Ingresa los números separados por espacio: ").split()))
resultado = math.prod(numeros)

print(resultado)  