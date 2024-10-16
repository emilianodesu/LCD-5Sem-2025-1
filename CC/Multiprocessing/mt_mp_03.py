'''
Llamaremos a nuestra función cpu_bound(), que toma un número grande (200,000,000) como parámetro
y lo decrementa en cada paso hasta que es cero. Se le pide a nuestra CPU que haga la cuenta
regresiva en cada llamada de función. Tenga en cuenta que una vez más es nuestro MainProcess
llamando a la función dos veces, una tras otra, en su hilo predeterminado, MainThread.
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
    cpu_bound(COUNT)
    cpu_bound(COUNT)


    end = time.time()
    print('Time taken in seconds -', end - start)
