#!/usr/bin/env python
"""reducer.py"""
import sys

current_word = None
current_count = 0
word = None
for line in sys.stdin:
    line = line.strip()
    # Separar los datos obtenidos de mapper.py
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        # Si no es un entero, se ignora
        continue
    # Este IF funciona porque Hadoop ordena la salida del mapper
    # por la clave (word) antes de pasarla al reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Escribir el resultado en la salida estandar
            print(f'{current_word}\t{current_count}')
        current_count = count
        current_word = word
    # Es necesario escribir la ultima palabra
if current_word == word:
    print(f'{current_word}\t{current_count}')

############################################################
# Ejecutar en consola:
# echo 'hola mundo cruel probando hola mundo adiós mundo cruel' \
# | ./ mapper2. py | sort -k1 ,1 | ./ reducer2.py
