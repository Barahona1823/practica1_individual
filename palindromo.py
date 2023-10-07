def es_palindroma(palabra):
    palabra = palabra.lower()  # Convertir a minúsculas para que sea insensible a mayúsculas
    palabra = palabra.replace(" ", "")  # Eliminar espacios en blanco
    return palabra == palabra[::-1]
