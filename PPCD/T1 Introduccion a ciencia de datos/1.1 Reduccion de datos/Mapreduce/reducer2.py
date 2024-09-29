#!/usr/bin/env python
"""Un reducer más avanzado con iteradores y generadores de Python"""
from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    """Parsea la salida del mapper y la convierte en pares clave-valor"""
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    """Reduce los datos de entrada y emite el resultado"""
    data = read_mapper_output(sys.stdin, separator=separator)
    # groupby agrupa múltiples contadores por palabra y crea un iterador
    # que devuelve claves consecutivas y su grupo asociado
    # current_word - la clave ( palabra )
    # group - iterador que entrega todas las parejas [ < current_word > , < count >]
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print(f'{current_word}{separator}{total_count}')
        except ValueError:
            # Si no se puede convertir a entero, ignorar la línea
            pass

if __name__ == "__main__":
    main()

####################################################
# Ejecutar en consola:
# echo 'hola mundo cruel probando hola mundo adiós mundo cruel' \
# | ./ mapper2. py | sort -k1 ,1 | ./ reducer2.py
