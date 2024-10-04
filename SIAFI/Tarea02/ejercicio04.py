"""Crea dos matrices de 3x3 con números enteros aleatorios y realiza
las operaciones de suma, resta y multiplicación de las matrices"""

import numpy as np

if __name__ == "__main__":
    matriz1 = np.random.randint(0, 10, (3, 3))
    matriz2 = np.random.randint(0, 10, (3, 3))
    print(f"Matriz 1:\n{matriz1}")
    print(f"Matriz 2:\n{matriz2}")
    print(f"Suma de matrices:\n{matriz1 + matriz2}")
    print(f"Resta de matrices:\n{matriz1 - matriz2}")
    print(f"Multiplicación de matrices:\n{matriz1 @ matriz2}")
