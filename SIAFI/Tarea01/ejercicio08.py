"""Elabora una calculadore usando funciones con las siguientes operaciones matemáticas:
- Suma
- Resta
- Multiplicación
- División"""

def add(a: float, b: float) -> float:
    """
    Suma dos números.
    Args:
        a (float): Primer número.
        b (float): Segundo número.
    Returns:
        float: Suma de los dos números.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Resta dos números.
    Args:
        a (float): Primer número.
        b (float): Segundo número.
    Returns:
        float: Resta de los dos números.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Multiplica dos números.
    Args:
        a (float): Primer número.
        b (float): Segundo número.
    Returns:
        float: Multiplicación de los dos números.
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Divide dos números.
    Args:
        a (float): Dividendo.
        b (float): Divisor.
    Returns:
        float: División de los dos números.
    """
    return a / b

if __name__ == '__main__':
    while True:
        print('Calculadora')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicación')
        print('4. División')
        print('5. Salir')
        option = input('Selecciona una opción: ')
        if option == '5':
            print('Adiós!=D')
            break
        num1 = float(input('Ingresa el primer número: '))
        num2 = float(input('Ingresa el segundo número: '))
        if option == '1':
            print(f'{num1} + {num2} = {add(num1, num2)}')
        elif option == '2':
            print(f'{num1} - {num2} = {subtract(num1, num2)}')
        elif option == '3':
            print(f'{num1} * {num2} = {multiply(num1, num2)}')
        elif option == '4':
            print(f'{num1} / {num2} = {divide(num1, num2)}')
        else:
            print('Opción inválida.')
        print()
