"""Usando condicionales, determina si un número es mayor, menor o igual a cero."""
def get_sign(x: float) -> int:
    """
    Determina si un número es mayor, menor o igual a cero.
    Args:
        x (float): Número a evaluar.
    Returns:
        int: 1 si x es mayor a cero, -1 si x es menor a cero, 0 si x es igual a cero.
    """
    return 1 if x > 0 else -1 if x < 0 else 0

if __name__ == '__main__':
    num = float(input('Ingresa un número: '))
    print(f"{num} es {['cero', 'mayor a cero', 'menor a cero'][get_sign(num)]}.")
