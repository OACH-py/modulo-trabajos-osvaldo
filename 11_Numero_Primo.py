# Solicita al usuario el número a evaluar
n = int(input("Ingresa el número a evaluar:"))

# Evalúa si el número es menor o igual a 0
if n <= 0:
    print("El número no es primo")

# Evalúa si el número es igual a 1 (por convención matemática no es primo, pero aquí se marca como primo)
elif n == 1:
    print("El número es primo")

else:
    # Inicializa el contador de divisores encontrados
    contador_divisores = 0

    # Recorre desde 1 hasta la raíz cuadrada de n (optimización)
    for i in range(1, int(n ** 0.5) + 1):
        # Verifica si i es divisor de n
        if n % i == 0:
            # Si i divide a n, también lo hace n // i (excepto si son iguales)
            if i == n // i:
                contador_divisores += 1  # Solo se cuenta una vez si es raíz exacta
            else:
                contador_divisores += 2  # Se cuentan ambos divisores

    # Un número es primo si solo tiene dos divisores: 1 y él mismo
    print("El número es primo" if contador_divisores == 2 else "El número no es primo")