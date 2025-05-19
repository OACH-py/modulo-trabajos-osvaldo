# Definición de la función 'rango_edad' que recibe un parámetro: edad
def rango_edad(edad):
    # Verifica si la edad es menor que 0; si lo es, devuelve un mensaje de error
    if edad < 0:
        return "Edad no válida"
    
    # Retorna una categoría según el rango en el que se encuentra la edad
    return (
        "Niñez" if edad <= 12 else         # De 0 a 12 años
        "Adolescencia" if edad <= 17 else  # De 13 a 17 años
        "Juventud" if edad <= 29 else      # De 18 a 29 años
        "Adultez" if edad <= 59 else       # De 30 a 59 años
        "Vejez (adulto mayor)"             # 60 años en adelante
    )

# Bloque principal de ejecución, que intenta obtener y procesar la entrada del usuario
try:
    # Solicita al usuario que introduzca su edad y convierte la entrada en un número entero
    edad = int(input("Introduce tu edad: "))
    
    # Llama a la función 'rango_edad' con la edad introducida y muestra el resultado
    print(f"Rango de edad: {rango_edad(edad)}")

# Captura el error si el usuario introduce un valor que no puede convertirse a entero
except ValueError:
    print("Edad inválida: ingresa un número entero.")
