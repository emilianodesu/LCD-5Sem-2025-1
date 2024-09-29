#!/usr/bin/env python
"""Un mapper más avanzado con iteradores y generadores de Python"""
import sys
def read_input(file):
    """Lee la entrada y la convierte en un generador de líneas"""
    for line in file:
        yield line.split()

def main(separator='\t'):
    """Lee la entrada y genera pares clave-valor"""
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            print(f'{word}{separator}1')

if __name__ == "__main__":
    main()

#######################################################
# Ejecutar en consola:
# echo 'hola mundo cruel probando hola mundo adiós mundo cruel' \
# | ./mapper2.py
