"""Usando condicionales, determina la clasificación de las calificaciones
de los siguientes miembros de SIAFI de acuerdo a la siguiente tabla:

- Yael: 70
- Ilse: 90
- Eduardo: 80

Calificación    | Clasificación
----------------|--------------
Entre 100 y 90  |       A
Entre 90 y 80   |       B
Entre 80 y 70   |       C
Entre 70 y 60   |       D
Menor a 60      |       F
"""

def get_grade(x: int) -> str:
    """
    Determina la clasificación de una calificación.
    Args:
        x (int): Calificación a evaluar.
    Returns:
        str: Clasificación de la calificación.
    """
    return 'A' if 90 <= x <= 100 else 'B' if 80 <= x < 90 \
    else 'C' if 70 <= x < 80 else 'D' if 60 <= x < 70 else 'F'

if __name__ == '__main__':
    students = {'Yael': 70, 'Ilse': 90, 'Eduardo': 80}
    for student, grade in students.items():
        print(f"{student}, calificación: {grade}, clasificación: {get_grade(grade)}.")
