"""Elabora una función que devuelva si un número es par o impar 
y que determine si es positivo, negativo o cero."""

def sign_and_parity(n: int) -> str:
    """
    Determina si un número es par o impar y si es positivo, negativo o cero.
    Args:
        n (int): Número a evaluar.
    Returns:
        str: Resultado de la evaluación.
    """
    if n == 0:
        return 'Cero'
    if n > 0:
        sign = 'Positivo'
    else:
        sign = 'Negativo'
    if n & 1:
        parity = 'Impar'
    else:
        parity = 'Par'
    return f'{sign} {parity}'

if __name__ == '__main__':
    number = int(input('Ingresa un número: '))
    print(sign_and_parity(number))
