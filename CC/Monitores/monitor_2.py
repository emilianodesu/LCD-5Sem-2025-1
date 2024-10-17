"""EJEMPLO wait/notify_all CON UNA CONDICIÓN"""

###### MODULOS ######
from time import sleep
from random import random
from threading import Thread
from threading import Condition

def task(condicion, number):
    """Funcion objetivo que simula un hilo esperando a ser notificado."""
    # Imprime el número de hilo
    print(f'Thread {number} waiting...')
    # Los hilos esperan a que sean notificados para continuar
    # 'with' es el equivalente a acquire/release.
    with condicion:
        # 'wait' espera hasta que se notifique o hasta que se agote el tiempo de espera.
        condicion.wait()
    # Después de ser liberados de la cola se duermen un tiempo aleatorio.
    value = random()
    sleep(value)
    # Los hilos imprimen el número aleatorio obtenido.
    print(f'Thread {number} got {value}')

##### INICIO #####
# Objeto condición.
condition = Condition()

# Crea 5 objetos tipo hilo y los inicia.
for i in range(5):
    worker = Thread(target=task, args=(condition, i))
    worker.start()
# El hilo principal duerme 3 segundos.
sleep(3)

# Notifica a todos los hilos que pueden continuar.
# 'with' Adquiere el monitor y es el equivalente a acquire/release.
with condition:
    #'notify_all' notifica a todos los hilos que pueden salir de la cola.
    # Como todos los hilos son notificados no necesariamente saldrán de la
    # variable condición en orden como llegaron.
    condition.notify_all()
