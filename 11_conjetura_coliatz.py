n = int(input("Valor inicial: "))
p = 0

def es_par(n):
    return n % 2 == 0

while n > 1:
    p += 1
    if es_par(n):
        print(n, "-> par, nuevo valor:", n // 2)
        n //= 2
    else:
        print(n, "-> impar, nuevo valor:", n * 3 + 1)
        n = n * 3 + 1

print("Pasos:", p)
