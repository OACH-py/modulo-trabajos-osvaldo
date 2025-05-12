# Solicita al usuario un número para generar su tabla de multiplicar
n = int(input("Ingresa el número para obtener la tabla: "))

# Inicializa una variable para almacenar la suma de los resultados
suma = 0

# Recorre los números del 1 al 10 para generar la tabla
for i in range(1, 11):
    # Calcula el producto del número ingresado por el valor actual del ciclo
    resultado = n * i
    
    # Imprime la operación y su resultado
    print(f"{n} * {i} = {resultado}")
    
    # Acumula el resultado en la variable suma
    suma += resultado

# Imprime la sumatoria total de todos los resultados de la tabla
print(f"Sumatoria es: {suma}")