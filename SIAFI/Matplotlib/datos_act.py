"""Gráfica de pastel"""

import matplotlib.pyplot as plt

# Datos de participación en actividades extracurriculares
data_actividades = {
    'Actividad': ['Deportes', 'Música', 'Artes', 'Ciencia', 'Club de Lectura'],
    'Participación': [40, 30, 20, 5, 5]
}

plt.pie(data_actividades['Participación'], labels=data_actividades['Actividad'], autopct='%1.1f%%')
plt.title('Participación en actividades extracurriculares')
plt.show()
