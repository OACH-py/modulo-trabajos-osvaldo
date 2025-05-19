# Función para convertir grados decimales a formato sexagesimal
def decimal_a_sexagesimal(decimal):
    # Separa la parte entera como grados
    grados = int(decimal)
    # Calcula los minutos a partir del decimal restante
    minutos_dec = (decimal - grados) * 60
    minutos = int(minutos_dec)
    # Calcula los segundos a partir del decimal restante de los minutos
    segundos = (minutos_dec - minutos) * 60
    # Imprime el resultado en formato sexagesimal
    print(f"{grados}° {minutos}' {segundos:.2f}''")

# Función para convertir grados sexagesimales a decimales
def sexagesimal_a_decimal(grados, minutos, segundos):
    # Realiza la conversión a grados decimales
    decimal = grados + minutos / 60 + segundos / 3600
    # Imprime el resultado en formato decimal con 6 decimales
    print(f"{decimal:.6f}°")

# Mostrar opciones al usuario
print("1. Decimal a sexagesimal")
print("2. Sexagesimal a decimal")

# Solicita la opción deseada
opcion = input("Elige una opción (1 o 2): ")

# Opción 1: decimal a sexagesimal
if opcion == "1":
    d = float(input("Ingresa los grados decimales: "))
    decimal_a_sexagesimal(d)

# Opción 2: sexagesimal a decimal
elif opcion == "2":
    g = int(input("Grados: "))
    m = int(input("Minutos: "))
    s = float(input("Segundos: "))
    sexagesimal_a_decimal(g, m, s)

# Opción no válida
else:
    print("Opción inválida.")