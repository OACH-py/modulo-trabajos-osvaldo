# 📊 **Documentación del Programa: Cálculos Básicos con Números**

## 📝 **Descripción General**

Este programa permite al usuario ingresar una lista de números separados por espacios. Luego, realiza los siguientes cálculos:

- **Suma** ➕: La suma total de los números.
- **Número más grande** 🔼: El valor más alto en la lista.
- **Número más pequeño** 🔽: El valor más bajo en la lista.
- **Promedio** 📉: El valor medio de los números.

El programa valida que la entrada sea correcta, asegurando que solo se ingresen números. En caso de un error, el usuario es informado y puede intentarlo nuevamente. 

---

## 🧑‍💻 **Estructura del Código**

El programa está estructurado de manera sencilla, utilizando un ciclo `while` para permitir que el usuario ingrese datos válidos, y un bloque `try-except` para manejar errores de entrada. A continuación, se presenta el código:

```python
# Inicia un ciclo infinito que se repetirá hasta que el usuario ingrese una entrada válida
while True:

    # Solicita al usuario que ingrese números separados por espacios
    numeros = input("Ingresa los números separados por espacio: ")

    try:
        # Divide la entrada por espacios y convierte cada elemento a tipo float
        lista = list(map(float, numeros.split()))

        # Calcula la suma de los números
        print(f"La suma es: {sum(lista)}")

        # Encuentra y muestra el número más grande
        print(f"El número más grande es: {max(lista)}")

        # Encuentra y muestra el número más pequeño
        print(f"El número más pequeño es: {min(lista)}")

        # Calcula el promedio: suma total entre cantidad de elementos
        promedio = sum(lista) / len(lista)
        print(f"El promedio es: {promedio}")

        # Si todo fue correcto, rompe el ciclo y termina
        break

    # Captura errores si el usuario ingresó un dato no numérico
    except ValueError:
        print("Error: Solo se permiten números. Intenta de nuevo.")
```
---

## 💡 **Explicación del Código**

1. **Entrada de Datos**:

   El programa solicita al usuario que ingrese una serie de números separados por espacios. Utiliza la función `input()` para capturar la entrada del usuario.

2. **Validación de Entrada**:

   El programa usa un bloque `try-except` para manejar posibles errores. Si el usuario ingresa algo que no sea un número (por ejemplo, texto), el bloque `except` captura ese error y muestra un mensaje de advertencia.

3. **Cálculos**:

   - **Suma** ➕: Utiliza la función `sum()` para obtener la suma total de los números ingresados.
   - **Máximo y Mínimo** 🔼🔽: Se usan las funciones `max()` y `min()` para encontrar los valores más alto y más bajo de la lista.
   - **Promedio** 📉: Se calcula dividiendo la suma total de los números entre la cantidad de elementos en la lista (`len(lista)`).

4. **Resultado**:

   Después de realizar los cálculos, el programa imprime la **suma**, el **número más grande**, el **número más pequeño** y el **promedio** en la consola.

---

## 🔑 **Conceptos Clave**

1. **`try` y `except`**:

   - **`try`**: Intenta ejecutar el bloque de código que sigue. Si no ocurre ningún error, el programa sigue con el flujo normal.
   - **`except`**: Captura cualquier error que ocurra en el bloque `try`. En este caso, se captura el error de conversión de datos cuando el usuario ingresa algo que no es un número.

2. **Funciones `sum()`, `max()`, `min()`, `len()`**:

   - **`sum()`** ➕: Calcula la suma total de los elementos de una lista.
   - **`max()`** 🔼: Devuelve el valor máximo de la lista.
   - **`min()`** 🔽: Devuelve el valor mínimo de la lista.
   - **`len()`** 📏: Devuelve la cantidad de elementos en la lista.

3. **Cálculo del Promedio** 📉:

   El promedio se calcula sumando todos los números y dividiendo el resultado entre la cantidad de elementos (`len(lista)`).

---

## 🖥️ **Ejemplo de Ejecución del Código**

Supón que el usuario ingresa los siguientes números:

**Entrada**:
Ingresa los números separados por espacio: 10 20 30 40 50

**Salida**:

La suma es: 150.0 El número más grande es: 50.0 El número más pequeño es: 10.0 El promedio es: 30.0