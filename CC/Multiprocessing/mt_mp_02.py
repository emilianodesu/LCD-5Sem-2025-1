'''
Usamos hilos en Python para acelerar la ejecución de las funciones. Los hilos
Thread-1 y Thread-2 son iniciados por nuestro MainProcess, cada uno de los cuales
llama a nuestra función, casi al mismo tiempo. Ambos subprocesos completan su trabajo
de dormir durante 10 segundos, al mismo tiempo. Esto redujo el tiempo total de
ejecución de todo nuestro programa en un significativo 50%. Por lo tanto, los hilos
múltiples son la solución ideal para ejecutar tareas en las que el tiempo de inactividad
de nuestra CPU se puede utilizar para realizar otras tareas. Por lo tanto, ahorrar
tiempo al hacer uso del tiempo de espera.
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
        ---> Start counting...")
 
    while n>0:
        n -= 1
 
    print(f"{pid} * {processName} * {threadName} \
        ---> Finished counting...")
 
if __name__=="__main__":
    start = time.time()
 
    # YOUR CODE SNIPPET HERE
    t1 = Thread(target = io_bound, args =(SLEEP, ))
    t2 = Thread(target = io_bound, args =(SLEEP, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


    end = time.time()
    print('Time taken in seconds -', end - start)
