"""Crea un array unidimensional con los números del 0 al 9 y encuentra
el número máximo, mínimo y la media de los valores del array."""

import numpy as np

if __name__ == "__main__":
    arreglo = np.array(list(range(10)))
    maximo = np.max(arreglo)
    minimo = np.min(arreglo)
    media = np.mean(arreglo)
    print(f"Arreglo: {arreglo}")
    print(f"Máximo: {maximo}")
    print(f"Mínimo: {minimo}")
    print(f"Promedio: {media}")
