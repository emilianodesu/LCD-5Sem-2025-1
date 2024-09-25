'''
Acabamos de demostrar que los subprocesos funcionaron sorprendentemente bien para múltiples tareas vinculadas a I/O.
Usemos el mismo enfoque para ejecutar nuestras tareas vinculadas a la CPU. Se inician los hilos al mismo tiempo, pero al final,
vemos que la ejecución completa del programa tomó un tiempo similar que cuando se llama la función io_bound().
¿Qué es lo que acaba de suceder? Esto se debe a que cuando se inició Thread-1, adquirió el Bloqueo de Intérprete Global (GIL)
que impidió que Thread-2 hiciera uso del CPU. Por lo tanto, Thread-2 tuvo que esperar a que Thread-1 terminara su tarea y
liberara el bloqueo para que pudiera realizar su tarea. Esta adquisición y liberación del bloqueo agregó una sobrecarga al
tiempo total de ejecución. Por lo tanto, podemos decir que la creación de hilos no es una solución ideal para
tareas que requieren que la CPU se ocupe en algún proceso.
'''

import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process
 
 
COUNT = 200000000
SLEEP = 10
 
def io_bound(sec):
 
    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name
 
    print(f"{pid} * {processName} * {threadName} \
        ---> Start sleeping...\n")
    time.sleep(sec)
    print(f"{pid} * {processName} * {threadName} \
        ---> Finished sleeping...\n")
 
def cpu_bound(n):
 
    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name
 
    print(f"{pid} * {processName} * {threadName} \
        ---> Start counting...\n")
 
    while n>0:
        n -= 1
 
    print(f"{pid} * {processName} * {threadName} \
        ---> Finished counting...\n")
 
if __name__=="__main__":
    start = time.time()
 
    # YOUR CODE SNIPPET HERE
    t1 = Thread(target = cpu_bound, args =(COUNT, ))
    t2 = Thread(target = cpu_bound, args =(COUNT, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end = time.time()
    print('Time taken in seconds -', end - start)
