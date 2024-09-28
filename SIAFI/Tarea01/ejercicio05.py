"""Completa el siguiente código para sólo imprimir los números pares

Código a completar:
for i in range(1,101):
"""

for i in range(1,101):
    if i & 1 == 0:
        print(i, end=' ')
