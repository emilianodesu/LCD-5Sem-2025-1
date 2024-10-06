"""Grafica de lineas"""
import matplotlib.pyplot as plt

# Datos de ventas mensuales
data_ventas = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    'Producto_A': [1500, 1800, 1700, 1900, 2200, 2100],
    'Producto_B': [2000, 2100, 2300, 2000, 1900, 2100],
    'Producto_C': [2300, 3000, 3200, 2600, 2700, 2900]
}

plt.plot(data_ventas['Mes'], data_ventas['Producto_A'], '*--', label='Producto A')
plt.plot(data_ventas['Mes'], data_ventas['Producto_B'], 'o--', label='Producto B')
plt.plot(data_ventas['Mes'], data_ventas['Producto_C'], 'x--', label='Producto C')
plt.title('Ventas mensuales')
plt.ylabel('Ventas [$]')
plt.legend(loc='best')
plt.show()
