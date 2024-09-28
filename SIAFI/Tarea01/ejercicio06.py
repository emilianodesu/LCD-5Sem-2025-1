"""Usando ciclos, calcula el promedio de sólamente los números positivos de la siguiente lista:

lista = [20, 50, -12, 6, -60, -5, 8, -14, 80, 90, -56, 50]
"""
def calculate_mean(lst: list) -> float:
    """
    Calcula el promedio de los números positivos de una lista.
    Args:
        lst (list): Lista de números.
    Returns:
        float: Promedio de los números positivos de la lista.
    """
    total = 0
    count = 0
    for i in lst:
        if i > 0:
            total += i
            count += 1
    return total / count

if __name__ == '__main__':
    lista = [20, 50, -12, 6, -60, -5, 8, -14, 80, 90, -56, 50]
    print(calculate_mean(lista))
