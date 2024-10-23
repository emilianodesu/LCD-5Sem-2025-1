"""SEMÁFORO USADO POR 6 HILOS"""

##### MODULOS #####
from threading import Thread, Semaphore
import time
##### FUNCIÓN #####

# Los hilos mandan llamar a wait (en python es 'acquire').

def muestra(the_name, num, semaforo):
    """Función que simula la entrada y salida de la sección crítica."""
    # Llamada a 'wait' del semáforo (en python es 'acquire').
    semaforo.acquire()

    # Imprime el nombre del hilo 4 veces antes de salir de la sección crítica.
    for _ in range(4):
        time.sleep(0.5)
        print(the_name,num)
    # Llamada a 'signal' del semáforo (en python es 'release').
    s.release()

##### INICIO #####

# Crea el objeto 's' de tipo 'Semaforo' y lo inicializa en 1.
s = Semaphore(1)

# Número de hilos
N_HILOS = 6

# Lista de almacenamiento de los objetos hilos
hilos = []

# Creación de los hilos.
for i in range(N_HILOS):
    hilo = Thread(target = muestra , args = ('Hilo ',i,s))

    # Almacena los objetos hilos
    hilos.append(hilo)

# Inicialización de hilos
for hilo in hilos:
    hilo.start()

# Espera a todos los hilos.
for hilo in hilos:
    hilo.join()
