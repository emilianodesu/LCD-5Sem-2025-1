""" CUENTA EL NUMERO DE HILOS ACTIVOS E IMPRIME INFORMACIÓN RELEVANTE """
import threading
import time
import os


##### Funciones para cada uno de los hilos #####
def hilo1_subroutine(i):
    """Funcion 1"""
    time.sleep(5)
    nombre = threading.current_thread().name
    print(nombre, "Número de proceso:         ", os.getpid())
    print(nombre, "Número de hilos activos:   ", threading.active_count())
    print(nombre, "ID:                        ",threading.get_ident())
    print(nombre, 'Value:                     ', i)
    print(nombre, "¿El hilo 1 está vivo?      ",hilo1.is_alive())
    print(nombre, "¿El hilo 2 está vivo?      ",hilo2.is_alive())
    print(nombre, "¿El hilo 3 está vivo?      ",hilo3.is_alive())


def hilo2_subroutine(i):
    """Funcion 2"""
    time.sleep(2)
    nombre = threading.current_thread().name
    print(nombre, "Número de proceso:         ", os.getpid())
    print(nombre, "Número de hilos activos:   ", threading.active_count())
    print(nombre, "ID:                        ",threading.get_ident())
    print(nombre, "Value:                     ", i)
    print(nombre, "¿El hilo 1 está vivo?      ",hilo1.is_alive())
    print(nombre, "¿El hilo 2 está vivo?      ",hilo2.is_alive())
    print(nombre, "¿El hilo 3 está vivo?      ",hilo3.is_alive())


def hilo3_subroutine(i):
    """Funcion 3"""
    time.sleep(10)
    nombre = threading.current_thread().name
    print(nombre, "Número de proceso:         ", os.getpid())
    nombre = threading.current_thread().name
    print(nombre, "Número de hilos activos:   ", threading.active_count())
    print(nombre, "ID:                        ",threading.get_ident())
    print(nombre, "Value:                     ", i)
    print(nombre, "¿El hilo 1 está vivo?      ",hilo1.is_alive())
    print(nombre, "¿El hilo 2 está vivo?      ",hilo2.is_alive())
    print(nombre, "¿El hilo 3 está vivo?      ",hilo3.is_alive())

##### Hilo principal #####

# Un hilo principal
print("Main INICIO: Número de hilos activos: ", threading.active_count())
print("Main INICIO: ID del hilo principal: ", threading.get_ident())

# Creacion de los objetos hilo1, hilo2 y hilo3.

hilo1 = threading.Thread(target=hilo1_subroutine, args=(100,), name="Thread 1")
hilo2 = threading.Thread(target=hilo2_subroutine, args=(200,), name="Thread 2")
hilo3 = threading.Thread(target=hilo3_subroutine, args=(300,), name="Thread 3")

print("Main Número de proceso:             ", os.getpid())



# Inicializa la ejecución de todos los hilos
hilo1.start()
hilo2.start()
hilo3.start()


hilo3.join() # El hilo principal espera a que termine el hilo 3.

print("Main: Número de hilos activos:        ", threading.active_count())
