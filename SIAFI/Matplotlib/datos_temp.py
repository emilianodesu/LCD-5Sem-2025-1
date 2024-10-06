"""Gráfica de barras"""

import matplotlib.pyplot as plt

# Datos de temperaturas diarias
data_temperaturas = {
    'Día': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'],
    'Ciudad_A': [22, 24, 23, 25, 26]
}

plt.bar(data_temperaturas['Día'], data_temperaturas['Ciudad_A'])
plt.title('Temperaturas diarias en Ciudad A')
plt.ylabel('T [°C]')
plt.show()
