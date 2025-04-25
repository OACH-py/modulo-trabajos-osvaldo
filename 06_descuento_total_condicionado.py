precio = float(input("Precio $: "))
cantidad = int(input("Cantidad: "))
descuento = int(input("Descuento %: "))
minimo_total_descuento = float(input("Total mínimo para aplicar descuento $: "))

subtotal = precio * cantidad

if subtotal > minimo_total_descuento:
    total = subtotal * (1 - descuento / 100)
else:
    total = subtotal

print(f"Total a pagar: ${total:.2f}, con un descuento de: {descuento}%")
