def calcular_descuento(venta_total: float):
    if 1000 <= venta_total <= 3000:
        return venta_total * 0.05
    elif 3001 <= venta_total <= 7000:
        return venta_total * 0.10
    elif 7001 <= venta_total <= 14000:
        return venta_total * 0.15
    elif 11001 <= venta_total <= 20000:
        return venta_total * 0.20
    elif venta_total > 20_000:
        return venta_total * 0.30
    else:
        return 0.0

def main():
    try:
        precio_unitario = float(input("Ingrese el precio unitario: "))
        cantidad = int(input("Ingrese la cantidad: "))
    except ValueError:
        print("Error: precio o cantidad no válidos.")
        return

    venta_total = precio_unitario * cantidad
    descuento = calcular_descuento(venta_total)
    venta_neta = venta_total - descuento

    print(f"Venta total:   ${venta_total:,.2f}")
    if descuento > 0:
        print(f"Descuento:     ${descuento:,.2f}")
    else:
        print("Descuento:     No aplica")
    print(f"Venta neta:    ${venta_neta:,.2f}")
main()