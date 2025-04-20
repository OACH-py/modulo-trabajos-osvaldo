def rango_edad(edad):
    if edad < 0:
        return "Edad no válida"
    return (
        "Niñez" if edad <= 12 else
        "Adolescencia" if edad <= 17 else
        "Juventud" if edad <= 29 else
        "Adultez" if edad <= 59 else
        "Vejez (adulto mayor)"
    )

try:
    edad = int(input("Introduce tu edad: "))
    print(f"Rango de edad: {rango_edad(edad)}")
except ValueError:
    print("Edad inválida: ingresa un número entero.")