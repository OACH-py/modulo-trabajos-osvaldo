# Solicita al usuario que ingrese el inicio y fin del rango
inicio = int(input("Ingresa el inicio del rango a buacar: "))
fin = int(input("Ingresa el final del rango: ")) + 1  # Se suma 1 para incluir el valor final

# Inicializa listas para almacenar números primos y no primos
no_primos = []
primos = []

# Recorre el rango de números desde 'inicio' hasta 'fin'
for n in range(inicio, fin):
    if n <= 0:  # Los números negativos y el cero no son primos
        no_primos.append(n)
    elif n == 1:  # El 1 se considera un caso especial (no es primo pero aquí lo agregan a primos)
        primos.append(n)
    else:
        es_primo = True  # Asume inicialmente que el número es primo
        
        # Comprueba si el número es divisible por algún entero desde 2 hasta la raíz cuadrada de n
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:  # Si n es divisible por i, entonces no es primo
                es_primo = False
                break  # Sale del bucle al encontrar un divisor
        
        # Clasifica el número según si es primo o no
        if es_primo:
            primos.append(n)
        else:
            no_primos.append(n)

# Muestra las listas de números primos y no primos, junto con sus sumatorias
print("Los primos son:", primos, "Su sumatoria es:", sum(primos))
print("Los no primos son:", no_primos, "Su sumatoria es:", sum(no_primos))