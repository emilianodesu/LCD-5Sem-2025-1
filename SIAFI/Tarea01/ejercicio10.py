"""Elabora una función que reciba un número n y devuelva
la suma de todos los números desde 1 hasta n."""

def sum_numbers(n: int) -> int:
    """
    Suma los números desde 1 hasta n.
    Args:
        n (int): Número límite.
    Returns:
        int: Suma de los números desde 1 hasta n.
    """
    return (n * (n + 1)) // 2

if __name__ == '__main__':
    number = int(input('Ingresa un número: '))
    print(sum_numbers(number))
