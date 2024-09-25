""" INICIA 5 HILOS, MANDAN LLAMAR A LA FUNCION 'worker',
CADA HILO DUERME UN TIEMPO ALEATORIO Y TERMINAN SU EJECUCION.
"""

##### MÓDULOS #####
import random
import threading
import time


# Función 'worker'.
def worker(name: str) -> None:
    """
    Función que simula un proceso de trabajo.
    """
    print(f'Started worker {name}')
    worker_time = random.choice(range(1, 5))
    time.sleep(worker_time)
    print(f'{name} worker finished in {worker_time} seconds')


# Permite que este archivo se pueda importar como módulo sin ejecutar las
# las lineas que se encuentran debajo.

if __name__ == '__main__':
    # Crea los 5 hilos y los inicializa.
    for i in range(5):
        thread = threading.Thread(
                target=worker,
                args=(f'hilo_{i}',),
                )
        thread.start()
