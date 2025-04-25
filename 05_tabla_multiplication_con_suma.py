n = int(input("Ingresa el numero para obtener la tabla: "))

suma = 0
for i in range(1,11):
    resultado = n * i
    print(f"{n} * {i} = {resultado}")
    suma += resultado
print(f"Sumatoria es: {suma}")