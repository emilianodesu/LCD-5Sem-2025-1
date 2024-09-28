"""Elabora una función que imprima los números impares de la siguiente lista:
lista = [11, 47, 96, 8, 5, -43, 91, 0, 41, 38, 33, 10]"""

def print_odd_numbers(lst: list) -> None:
    """
    Imprime los números impares de una lista.
    Args:
        lst (list): Lista de números.
    """
    for i in lst:
        if i & 1:
            print(i, end=' ')

if __name__ == '__main__':
    lista = [11, 47, 96, 8, 5, -43, 91, 0, 41, 38, 33, 10]
    print_odd_numbers(lista)
