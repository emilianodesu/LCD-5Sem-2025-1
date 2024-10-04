"""Crea un DatFrame con 5 ciudades y su temperatura en grados Celsius.
Añade una nueva columna que convierta las temperaturas a Fahrenheit."""

import pandas as pd

if __name__ == '__main__':
    ciudades = ['Ciudad de México', 'Toluca', 'Puebla', 'Saltillo', 'Villahermosa']
    temperaturas = [20, 15, 25, 10, 30]
    df = pd.DataFrame({'T_C': temperaturas}, index=ciudades)
    df['T_F'] = df['T_C'] * 9/5 + 32
    print(df)
