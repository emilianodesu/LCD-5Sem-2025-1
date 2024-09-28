"""Imprime la tabla de multiplicar de un número n."""
def print_multiplication_table(n: int) -> None:
    """
    Imprime la tabla de multiplicar de un número n.
    Args:
        n (int): Número a multiplicar.
    """
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

if __name__ == '__main__':
    num = int(input('Ingresa un número entero: '))
    print_multiplication_table(num)
