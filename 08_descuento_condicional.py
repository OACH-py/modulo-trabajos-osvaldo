# Función que calcula el descuento basado en el monto total de la venta
def calcular_descuento(venta_total: float):
    if 1000 <= venta_total <= 3000:
        return venta_total * 0.05  # 5% de descuento
    elif 3001 <= venta_total <= 7000:
        return venta_total * 0.10  # 10% de descuento
    elif 7001 <= venta_total <= 14000:
        return venta_total * 0.15  # 15% de descuento
    elif 11001 <= venta_total <= 20000:
        return venta_total * 0.20  # 20% de descuento
    elif venta_total > 20_000:
        return venta_total * 0.30  # 30% de descuento
    else:
        return 0.0  # No aplica descuento


# Función principal que gestiona la entrada del usuario y muestra los resultados
def main():
    try:
        # Solicita al usuario el precio unitario y la cantidad de productos
        precio_unitario = float(input("Ingrese el precio unitario: "))
        cantidad = int(input("Ingrese la cantidad: "))
    except ValueError:
        # Maneja errores en caso de que la entrada no sea válida
        print("Error: precio o cantidad no válidos.")
        return

    # Calcula el total de la venta
    venta_total = precio_unitario * cantidad

    # Calcula el descuento aplicable
    descuento = calcular_descuento(venta_total)

    # Calcula la venta neta después de aplicar el descuento
    venta_neta = venta_total - descuento

    # Muestra los resultados
    print(f"Venta total:   ${venta_total:,.2f}")
    if descuento > 0:
        print(f"Descuento:     ${descuento:,.2f}")
    else:
        print("Descuento:     No aplica")
    print(f"Venta neta:    ${venta_neta:,.2f}")


# Ejecuta la función principal
main()