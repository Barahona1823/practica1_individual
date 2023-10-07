def fibonacci(n):
    if n <= 0:
        return "El número de Fibonacci no está definido para n <= 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n):
            next_fib = fib[i - 1] + fib[i - 2]
            fib.append(next_fib)
        return fib[-1]

# Ejemplo de uso
n = 10  # Cambia esto al número de Fibonacci que desees calcular
result = fibonacci(n)
print(f"El número de Fibonacci en la posición {n} es {result}")
