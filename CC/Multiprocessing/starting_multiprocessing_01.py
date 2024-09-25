"""SUMA DE NÚMEROS DE UNA LISTA USANDO 2 PROCESOS CON UNA VARIABLE COMPARTIDA
DECREMENTA 'n' DE 1 EN 1 HASTA 0. SE USA EL MÓDULO MULTIPROCESSING
"""

##### MÓDULOS #####
import time
from multiprocessing import Process,Value,Lock,current_process

##### FUNCIONES #####
def for1(num, suma_total,lock):
    """Calcula la suma de la primera mitad de números de la lista con 'pr1'."""
    suma_parcial = 0
    n = len(num) * 30
    print(f"En el proceso:                            {current_process().name}")
    print(f"Números en el proceso pr1:                 {len(num):,}")
    print("Calcula la suma de la primera mitad de números de la lista con 'pr1'.")

    for i in num:
        suma_parcial += i
    print(f"La suma parcial del proceso 'pr1' es:     {suma_parcial:.8e}")

    # Cualquier otra operación que dure gran cantidad de tiempo
    while n>0:
        n -= 1

    # Manda llamar al bloqueo
    lock.acquire()

    # Sección crítica
    # Para acceder a la variable compartida se usa '.value'.
    suma_total.value = suma_total.value + suma_parcial

    # Libera al bloqueo
    lock.release()

def for2(num,suma_total,lock):
    """Calcula la suma de la segunda mitad de números de la lista con  'pr2'."""
    suma_parcial = 0
    n = len(num) * 30

    print(f"En el proceso:                            {current_process().name}")
    print(f"Números en el proceso pr2:                 {len(num):,}")
    print("Calcula la suma de la segunda mitad de números de la lista con  'pr2'")

    for i in num:
        suma_parcial = suma_parcial + i

    print(f"La suma parcial del proceso 'pr2' es:     {suma_parcial:.8e}")

    # Cualquier otra operación que dure gran cantidad de tiempo
    while n>0:
        n -= 1

    # Sección crítica
    lock.acquire()
    # Para acceder a la variable compartida se usa '.value'.
    suma_total.value = suma_total.value + suma_parcial
    lock.release()

##### INICIO #####
if __name__ == "__main__":

    # Tiempo de inicio
    T1 = time.time()

    # Crea el objeto bloqueo
    bloqueo = Lock()

    # Variable compartida inicializada en '0', la 'd' significa flotante de precisión doble.
    la_suma_total = Value('d', 0)

    # Lista de números
    numeros = list(range(20000000))

    # Variables 'mitad' y 'total' del arreglo 'numeros'.
    mitad = int(len(numeros)/2)
    total = int(len(numeros))

    # Creación de los objetos tipo multiprocessing 'pr1' y 'pr2'.
    pr1 = Process(target=for1, args=(numeros[0:mitad],la_suma_total,bloqueo))
    pr2 = Process(target=for2, args=(numeros[mitad:total],la_suma_total,bloqueo))


    # Activación de los procesos 'pr1' y 'pr2'.
    t_activ1 = time.time() # Tiempo de inicio de activación de los procesos.
    pr1.start()
    pr2.start()
    t_activ2 = time.time() # Tiempo final de activación de los procesos.
    print(f"Tiempo de activación de los procesos      {t_activ2 - t_activ1}")

    # El programa espera a que terminen los 2 procesos.
    t_esp1 = time.time() # Tiempo de inicio de activación de los procesos.
    pr1.join()
    pr2.join()
    t_esp2 = time.time() # Tiempo de inicio de activación de los procesos.
    print(f"Tiempo de espera de los procesos         {t_esp2 - t_esp1}")


    # tiempo final del programa
    T2 = time.time()
    print(f"Nuevamente en el proceso principal:       {current_process().name}")
    print(f"La summa total es:                        {la_suma_total.value:.8e}")
    print(f"Tiempo total:                            {T2 - T1}")
