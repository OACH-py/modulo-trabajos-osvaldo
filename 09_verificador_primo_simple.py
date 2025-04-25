n = int(input("Ingresa el número a evaluar:"))
if n <= 0 :
    print("El número no es primo")
elif n == 1:
    print("El número es primo")
else:
    contador_divisores = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            contador_divisores += 1 
print("El número es primo" if contador_divisores == 2 else "El número no es primo")