"""CALCULA EL CUADRADO Y EL CUBO DE UNA LISTA USANDO 2 HILOS
MULTITHREADING ES CONVENIENTE CUANDO LOS HILOS
DUERMEN UN PERIODO DE TIEMPO O EN FUNCIONES DE I/O."""

##### Módulos #####
import time
import threading


##### Funciones #####
def cal_sqre(num):
    """Calcula el cuadrado de los elementos de un arreglo, este método lo invoca 'th1'."""
    print(" Calcula el cuadrado de los elementos de un arreglo")
    for n in num:
        time.sleep(0.3)
        print(f" El cuadrado de {n} :  {n * n}")

def cal_cube(num):
    """Calcula el cubo de los elementos de un arreglo, este método lo invoca 'th2'.s"""
    print(" Calcula el cubo de los elementos de un arreglo")
    for n in num:
        time.sleep(0.3)
        print(f" El cubo de {n} :  {n * n * n}")


##### Inicio #####
ar = [4, 5, 6, 7, 2]
t = time.time()

# Creación de los objetos tipo Thread 'th1' y 'th2'.
th1 = threading.Thread(target=cal_sqre, args=(ar,))
th2 = threading.Thread(target=cal_cube, args=(ar,))

# Activación de los hilos 'th1' y 'th2'.
th1.start()
th2.start()

# El programa espera a que terminen los 2 hilos.
th1.join()
th2.join()

print(" Tiempo total del programa :", time.time() - t)
print(" Nuevamente en el hilo principal")
