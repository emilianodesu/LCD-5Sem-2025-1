"""Crea una matriz de 3x3 con valores de 0 y otra con valores de 0
y otra con valores de 1."""

import numpy as np

if __name__ == "__main__":
    matriz_ceros = np.zeros((3, 3))
    matriz_unos = np.ones((3, 3))
    print(f"Matriz de ceros:\n{matriz_ceros}")
    print(f"Matriz de unos:\n{matriz_unos}")
