"""EJEMPLO DE acquire, release, wait, notify CON UNA CONDICIÓN
Comentar el Bloque 1 y descomentar el Bloque 2
"""


##### MODULOS #####

from time import sleep
from threading import Thread
from threading import Condition


##### FUNCIÓN QUE PREPARA ALGÚN TRABAJO #####

def task(condicion, lista):
    """Tarea que se ejecuta en un hilo."""
    # Duerme.
    sleep(3)
    # Imprime que está enviando la notificación.
    print('Thread sending notification...')

    # # ----------- Bloque 1. acquiere/release ---------
    # # Adquiere el monitor.
    # condicion.acquire()
    # # Agrega un dato a la lista de trabajo.
    # lista.append(33)
    # # Notifica a un hilo que el trabajo se ha realizado.
    # condicion.notify()
    # # Libera el monitor.
    # condicion.release()
    # # ----------- Bloque 1. acquiere/release ---------

    # ----------- Bloque 2. with ---------
    # acquire() y release() se sustituyen por 'with'.
    with condicion:
        # Agrega un dato a la lista de trabajo.
        lista.append(33)
        # Notifica a un hilo que el trabajo se ha ralizado.
        condicion.notify()
    # ----------- Bloque 2. with ---------

##### INICIO #####
# Crea un objeto condición.
condition = Condition()
# Un objeto lista.
work_list = []
# Imprime que el hilo principal está esperando el dato.
print('Main thread waiting for data...')
# Crea el objeto hilo 'worker'.
worker = Thread(target=task, args=(condition, work_list))
# Inicia el hilo
worker.start()
# Adquiere y libera el monitor.
# 'with' adquiere el monitor y es equivalente a 'acquire' y después 'release'.
with condition:
    # El hilo principal espera la notificación para continuar.
    condition.wait()
# Imprime la lista 'work_list'.
print(f'Got data: {work_list}')
