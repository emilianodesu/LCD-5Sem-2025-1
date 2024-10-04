"""Dado un array de 1o elementos, selecciona los valores que son mayores a 5.
Reemplaza los valores mayores a 8 por 0"""

import numpy as np
if __name__ == "__main__":
    array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"Array original:\n{array}")
    print(f"Valores mayores a 5:\n{array[array > 5]}")
    array[array > 8] = 0
    print(f"Reemplazando valores mayores a 8 por 0:\n{array}")
