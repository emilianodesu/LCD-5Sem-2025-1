"""Escribe una función que determine si una palabra o frase es un palíndromo."""

def is_palindrome(word: str) -> bool:
    """
    Determina si una palabra o frase es un palíndromo.
    
    Args:
        word (str): Palabra o frase a evaluar.
    
    Returns:
        bool: True si es palíndromo, False en caso contrario.
    """
    word = word.lower()
    return word == word[::-1]

if __name__ == '__main__':
    palabra = input('Ingresa una palabra: ')
    print(is_palindrome(palabra))
