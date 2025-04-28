# Solicita al usuario el precio unitario del producto

precio = float(input("Precio $: "))

# Solicita al usuario la cantidad de productos
cantidad = int(input("Cantidad: "))

# Solicita al usuario el porcentaje de descuento a aplicar
descuento = int(input("Descuento %: "))

# Solicita la cantidad necesaria para aplicar el descuento
min_cantidad = int(input("Cantidad mínima para aplicar descuento: "))

# Calcula el subtotal de la compra sin aplicar descuento
subtotal = precio * cantidad

# Verifica si la cantidad supera el mínimo requerido para aplicar el descuento

if cantidad >= min_cantidad:
    # Calcula el total aplicando el descuento
    total = subtotal * (1 - descuento / 100)
else:
    # El total es igual al subtotal si no se cumple la condición
    total = subtotal

# Imprime el total a pagar, mostrando el descuento aplicado en su caso
print(f"Total a pagar: ${total:.2f}, con un descuento del: {descuento}%")