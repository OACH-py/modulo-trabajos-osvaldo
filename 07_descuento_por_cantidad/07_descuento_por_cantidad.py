precio = float(input("Precio $: "))
cantidad = int(input("Cantidad: "))
descuento = int(input("Descuento %: "))
min_cantidad = int(input("Cantidad mínima para aplicar descuento: "))

subtotal = precio * cantidad

if cantidad >= min_cantidad:
    total = subtotal * (1 - descuento / 100)
else:
    total = subtotal

print(f"Total a pagar: ${total:.2f}, con un descuento del: {descuento}%")