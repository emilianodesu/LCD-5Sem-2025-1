"""
SE USAN 2 PROCESOS PARA ACCEDER A UNA VARIABLE COMPARTIDA Y 2 PROCESOS PARA UN ARREGLO COMPARTIDO
"""

##### MÓDULOS #####
from multiprocessing import Lock
from multiprocessing import Process, Value, Array
import time


##### FUNCIONES #####
def add_100(number, lock):
    """Función que incrementa 100 veces la variable compartida."""
    for _ in range(100):
        time.sleep(0.01)

        # Manda llamar al bloqueo
        lock.acquire()

        # Sección crítica
        number.value += 1

        # Libera al bloqueo
        lock.release()

def add_100_array(numbers, lock):
    """Función que incrementa 100 veces cada elemento del arreglo compartido."""
    for _ in range(100):
        time.sleep(0.01)
        for i, _ in enumerate(numbers):
            # Manda llamar al bloqueo
            lock.acquire()
            # Sección crítica
            numbers[i] += 1
            # Libera al bloqueo
            lock.release()


##### INICIO #####
if __name__ == "__main__":
    # Objeto bloqueo
    a_lock = Lock()

    # Variable compartida
    shared_number = Value('i', 0)
    print('Value at beginning:', shared_number.value)

    # Arreglo compartido
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at beginning:', shared_array[:])


    # Creación de los objetos tipo multiprocessing.
    process1 = Process(target=add_100, args=(shared_number, a_lock))
    process2 = Process(target=add_100, args=(shared_number, a_lock))
    process3 = Process(target=add_100_array, args=(shared_array, a_lock))
    process4 = Process(target=add_100_array, args=(shared_array, a_lock))


    # Activación de los 4 procesos.
    process1.start()
    process2.start()
    process3.start()
    process4.start()

    # El programa espera a que terminen los 4 procesos.
    process1.join()
    process2.join()
    process3.join()
    process4.join()

    # Impresión de los valores de la variable compartida y arreglo compartido.
    print('Value at end:', shared_number.value)
    print('Array at end:', shared_array[:])
    print('end main')
