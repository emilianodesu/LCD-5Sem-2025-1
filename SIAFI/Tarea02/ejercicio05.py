"""Crea una serie de 10 elementos con los números del 1 al 10.
Cambia los índices de la serie por los nomnres de los primeros
10 países según su población."""

import pandas as pd

if __name__ == "__main__":
    serie = pd.Series(range(1, 11))
    serie.index = ["China", "India", "Estados Unidos", "Indonesia", "Pakistán",
                   "Brasil", "Nigeria", "Bangladesh", "Rusia", "México"]
    print(serie)
