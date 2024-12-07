"""Usando condicionales, determina si un número es par o impar."""
def get_parity(x: int) -> str:
    """
    Determina si un número es par o impar.
    Args:
        x (int): Número a evaluar.
    Returns:
        str: 'par' si x es par, 'impar' si x es impar.
    """
    return 'par' if x & 1 == 0 else 'impar'

if __name__ == '__main__':
    num = int(input('Ingresa un número entero: '))
    print(f"{num} es {get_parity(num)}.")
