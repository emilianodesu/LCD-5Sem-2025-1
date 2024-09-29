#!/usr/bin/env python
"""mapper.py"""
import sys

# Los datos vienen de la entrada estandar (STDIN)
for line in sys.stdin:
    # Eliminar espacios en blanco
    line = line.strip()
    # Separar las palabras
    words = line.split()
    # Incrementar contadores
    for word in words:
        # Escribir el resultado en la salida estandar
        # Esta salida será la entrada para el reducer.py
        # Separado por tabulador, cada palabra cuenta 1
        print(f'{word}\t{1}')

############################################################
# Ejecutar en consola:
# echo 'hola mundo cruel probando hola mundo adiós mundo cruel' \
# | ./mapper.py
