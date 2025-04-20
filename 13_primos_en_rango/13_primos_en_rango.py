inicio = int(input("Ingresa el inicio del rango a buacar: "))
fin = int(input("Ingresa el final del rango: ")) + 1

no_primos = []
primos = []

for n in range(inicio , fin):
    if n <= 0 :
        no_primos.append(n)
    elif n == 1:
        primos.append(n)
    else:
        es_primo = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(n)
        else:
            no_primos.append(n)

print("Los primos son:", primos, "Su sumatoria es:", sum(primos))
print("Los no primos son:", no_primos, "Su sumatoria es:", sum(no_primos))