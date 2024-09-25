'''
Observamos cómo el multiprocessing nos ayuda a lograr el paralelismo, intentaremos usar esta técnica
para ejecutar tareas de I/O. Dado que los procesos Process-1 y Process-2 están realizando la tarea de
inactividad en su propio núcleo de CPU, no encontramos un beneficio evidente. Pero la creación de
procesos en sí es una tarea pesada para la CPU y requiere más tiempo que la creación de hilos.
Además, los procesos requieren más recursos que los hilos. Por lo tanto, siempre es mejor tener el
multiprocesamiento como la segunda opción para las tareas vinculadas a I/O, siendo el multitreading la
primera opción.
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
    p1 = Process(target = io_bound, args =(SLEEP, ))
    p2 = Process(target = io_bound, args =(SLEEP, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()
    print(f"ID del proceso principal: {os.getpid()}, nombre {current_process().name}, nombre del hilo: {current_thread().name}")
    print('Time taken in seconds -', end - start)

    
