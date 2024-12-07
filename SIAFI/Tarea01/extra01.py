"""Escribe una función que genere los primeros n números
de la secuencia de Fibonacci."""

def fibonacci(n: int, fib1: int = 0, fib2: int = 1, sequence=None) -> list:
    """
    Genera los primeros n números de la secuencia de Fibonacci.
    
    Args:
        n (int): Número de elementos a generar.
        fib1 (int): Primer número de la secuencia.
        fib2 (int): Segundo número de la secuencia.
        sequence (list): Lista para almacenar los números de Fibonacci.
    
    Returns:
        list: Lista con los primeros n números de Fibonacci.
    """
    if sequence is None:
        sequence = []
    if n == 0:
        return sequence
    sequence.append(fib1)
    return fibonacci(n-1, fib2, fib1+fib2, sequence)

if __name__ == '__main__':
    number = int(input('Ingresa un número: '))
    print(fibonacci(number))
