def cobrar_con_descuento(precio, descuento, cantidad):
    """
    Esta función calcula el precio después de aplicar un descuento.
    """
    precio_final = precio * cantidad - (precio * (descuento / 100))
    return precio_final

def main():
    """
    Función principal que solicita al usuario el precio y el descuento, y muestra el precio final.
    """
    # Solicita al usuario el precio del producto
    precio = float(input("Ingresa el precio del producto: "))
    
    # Solicita al usuario la cantidad de productos
    cantidad = int(input("Ingresa la cantidad de productos: "))
    
    # Solicita al usuario el porcentaje de descuento
    descuento = 10  # Descuento fijo del 10%
    
    # Calcula el precio final aplicando el descuento
    precio_final = cobrar_con_descuento(precio, descuento, cantidad)
    
    # Muestra el precio final
    print(f"El precio final después de aplicar un descuento del {descuento}% es: {precio_final:.2f}")

main()