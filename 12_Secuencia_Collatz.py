# Solicita al usuario el valor inicial para iniciar la secuencia
n = abs(int(input("Valor inicial: ")))

# Inicializa el contador de pasos
p = 0

# Define una función que determina si un número es par
def es_par(n):
    return n % 2 == 0

# Ejecuta el proceso mientras el número sea mayor que 1
while n > 1:
    # Incrementa el contador de pasos
    p += 1

    # Si el número es par, se divide entre 2
    if es_par(n):
        print(n, "-> par, nuevo valor:", n // 2)
        n //= 2
    # Si el número es impar, se multiplica por 3 y se suma 1
    else:
        print(n, "-> impar, nuevo valor:", n * 3 + 1)
        n = n * 3 + 1

# Imprime el número total de pasos realizados
print("Pasos:", p)