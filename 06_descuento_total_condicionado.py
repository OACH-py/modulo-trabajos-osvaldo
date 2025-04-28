# Solicita al usuario el precio unitario del producto
precio = float(input("Precio $: "))

# Solicita al usuario la cantidad de productos
cantidad = int(input("Cantidad: "))

# Solicita al usuario el porcentaje de descuento a aplicar
descuento = int(input("Descuento %: "))

# Solicita el monto mínimo necesario para aplicar el descuento
minimo_total_descuento = float(input("Total mínimo para aplicar descuento $: "))

# Calcula el subtotal de la compra sin aplicar descuento
subtotal = precio * cantidad

# Verifica si el subtotal supera el mínimo requerido para aplicar el descuento
if subtotal > minimo_total_descuento:
    # Calcula el total aplicando el descuento
    total = subtotal * (1 - descuento / 100)
else:
    # El total es igual al subtotal si no se cumple la condición
    total = subtotal

# Imprime el total a pagar, mostrando el descuento aplicado en su caso
print(f"Total a pagar: ${total:.2f}, con un descuento de: {descuento}%")