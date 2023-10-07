# Función para la multiplicación
def multiplicacion(a, b):
    return a * b

# Función para la división con validación de división entre cero
def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b
