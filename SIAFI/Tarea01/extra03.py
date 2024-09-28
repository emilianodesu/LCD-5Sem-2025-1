"""Escribe una función que calcule el factorial de un número."""
def factorial(n: int) -> int:
    """
    Calcula el factorial de un número.
    
    Args:
        n (int): Número a calcular su factorial.
    
    Returns:
        int: Factorial de n.
    """
    if n == 0:
        return 1
    return n * factorial(n-1)

if __name__ == '__main__':
    number = int(input('Ingresa un número: '))
    print(factorial(number))
