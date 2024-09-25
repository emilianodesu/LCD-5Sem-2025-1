'''
Le pedimos a nuestra CPU que ejecute la función io_bound(),
que toma un número entero (10) como parámetro y le pide a la CPU
que duerma durante esa cantidad de segundos. Esta ejecución tarda un total
de 20 segundos, ya que la ejecución de cada función tarda 10 segundos en
completarse. Tenga en cuenta que es el mismo MainProcess el que llama a
nuestra función dos veces, una tras otra, utilizando su hilo
predeterminado, MainThread.
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
 
    # Aquí puede agregarse un fragmento de código.
    
    io_bound(SLEEP)
    io_bound(SLEEP) 


    end = time.time()
    print('Time taken in seconds -', end - start)
