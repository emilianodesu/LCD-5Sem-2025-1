"""Del archivo ventas.csv, carga el dataframe y calcula el promedio de ventas"""

import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('ventas.csv')
    print(f'Promedio de ventas: {df['Ventas'].mean()}')
