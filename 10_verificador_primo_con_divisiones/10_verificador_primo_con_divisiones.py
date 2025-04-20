n = int(input("Ingresa el valor a evaluar: "))
contador_0 = 0

for i in range(1, n + 1):
    d = n % i
    print(n, "%", i,"=",d)
    if d == 0:
        contador_0 += 1
if contador_0 == 2:
    print("El numero es Primo")
else:
    print("El numero no es Primo")