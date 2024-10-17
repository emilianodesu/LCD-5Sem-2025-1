"""EJEMPLO wait_for  con una condición"""

##### MÓDULOS #####
from time import sleep
from random import random
from threading import Thread
from threading import Condition
from threading import current_thread

##### FUNCIÓN OBJETIVO #####
def task(condicion, lista):
    """Función objetivo que simula un hilo esperando a ser notificado."""
    h_nombre = current_thread().name
    # Adquiere y libera el monitor.
    with condicion:
        # Valor aleatorio.
        value = random()

        # Duerme un tiempo aleatorio.
        sleep(value)
        # Cada hilo agrega un valor a la lista.
        lista.append(value)

        # Imprime el nombre del hilo y el valor obtenido.
        print(f"Hilo {h_nombre} agregó {value}")
        # Notifica al hilo en espera.
        condicion.notify()


##### INICIO #####
# Objeto condición.
condition = Condition()
# Lista 'work_list'.
work_list = []
# Crea 5 hilos y los inicializa.
for i in range(5):
    worker = Thread(target=task, args=(condition, work_list))
    worker.start()
# El hilo principal espera a que todos los hilos agreguen su dato aleatorio a la lista.
with condition:
    # wait_for(predicate, timeout=None). Espera hasta que una condición se evalúe como verdadera.
    # 'predicate' se interpretará como un valor booleano.
    # Espera a que todos los hilos agreguen su valor correspondiente a la lista 'work_list'.
    # Una función 'lambda' o anónima para evaluar la longitud de la lista 'work_list'.
    condition.wait_for(lambda: len(work_list)==5)

    # # Si solo se coloca 'wait_for' sin 'predicate' marca un error.
    # condition.wait_for()

    # # Si solo se coloca 'wait' el hilo principal permanece bloqueado y no imprime la última línea.
    # condition.wait()

    # Imprime el contenido de la lista 'ork_list'.
    print(f"La lista 'work_list': {work_list}")
