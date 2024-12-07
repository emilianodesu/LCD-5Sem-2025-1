"""Crea un DataFrame con las columnas nombre, edad, y ciudad para
5 personas (ponle los datos que desees).
Añade una nueva columna llamada ocupación con valores de tu elección."""

import pandas as pd

if __name__ == '__main__':
    datos = {
        'nombre': ['Erling', 'Cristiano', 'Pedri', 'Lionel', 'Kylian'],
        'edad': [25, 30, 35, 40, 45],
        'ciudad': ['Ciudad de México', 'Guadalajara', 'Monterrey', 'Puebla', 'Veracruz']
    }
    df = pd.DataFrame(datos)
    df['ocupación'] = ['Ingeniero', 'Doctor', 'Abogado', 'Contador', 'Profesor']
    print(df)
