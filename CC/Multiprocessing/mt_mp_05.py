'''
El multiprocessing es la respuesta. Aquí, MainProcess genera procesos, que tienen diferentes PID (Identificador de Proceso).
Cada proceso se ejecuta en paralelo, haciendo uso de un núcleo de CPU separado y su propia instancia del intérprete de Python.
Hay que tener en cuenta que la salida puede imprimirse de forma desordenada ya que los procesos son independientes entre sí.
Cada proceso ejecuta la función en su propio hilo MainThread.
Observmos que el tiempo que tarda todo el programa es de aproximadamente la mitad que si se usaran hilos concurrentes en un solo
core.
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
    p1 = Process(target = cpu_bound, args =(COUNT, ))
    p2 = Process(target = cpu_bound, args =(COUNT, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()
    print('Time taken in seconds -', end - start)
