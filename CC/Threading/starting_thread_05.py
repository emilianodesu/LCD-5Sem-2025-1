"""SUMA DE NÚMEROS DE UNA LISTA USANDO 2 HILOS CON UNA VARIABLE COMPARTIDA
##### DECREMENTA 'n' DE 1 EN 1 HASTA 0. SE USA EL MÓDULO THREADING"""

##### MÓDULOS #####
import time
import threading


###### Variable global #####
suma_total = 0


##### MÉTODOS #####
def for1(num, bloqueo):
    """Calcula la suma de la primera mitad de números de la lista con 'th1'."""
    n = len(num) * 30
    print(f"Números calculados por hilo th1:        {len(num):,}")
    global suma_total
    suma_parcial = 0
    print("Calcula la suma de la primera mitad de números de la lista con 'th1'.")

    for i in num:
        suma_parcial = suma_parcial + i
    print(f"La suma parcial del hilo 'th1' es:        {suma_parcial:.8e}")
    # Cualquier otra operación que dure gran cantidad de tiempo
    while n>0:
        n -= 1

    # Sección critica
    bloqueo.acquire()
    suma_total = suma_total + suma_parcial
    bloqueo.release()

def for2(num, bloqueo):
    """Calcula la suma de la segunda mitad de números de la lista con 'th1'."""
    n = len(num) * 30
    print(f"Números calculados por hilo th2:        {len(num):,}")
    global suma_total
    suma_parcial = 0
    print("Calcula la suma de la segunda mitad de números de la lista con 'th2'.")

    for i in num:
        suma_parcial = suma_parcial + i

    print(f"La suma parcial del hilo 'th2' es:        {suma_parcial:.8e}")

    # Cualquier otra operación que dure gran cantidad de tiempo
    while n>0:
        n -= 1

    # Sección critica

    bloqueo.acquire()
    suma_total = suma_total + suma_parcial
    bloqueo.release()

##### INICIO #####

# Tiempo de inicio
T1 = time.time()

# Crea el objeto bloqueo
el_bloqueo = threading.Lock()

# Lista de números
# La lista va de 0 - 19999999
numeros = list(range(20000000))

# mitad = 10,000,000
mitad = int(len(numeros)/2)

# total = 20,000,000
total = int(len(numeros))

# Creación de los objetos tipo Thread 'th1' y 'th2'.

# La porcion del arreglo de numeros va de 0 - 9,999,999 (en total son 10 millones)
th1 = threading.Thread(target=for1, args=(numeros[0:mitad],el_bloqueo))

# La porcion del arreglo de numeros va de 10,000,000 - 19,999,999 (en total son 10 millones)
th2 = threading.Thread(target=for2, args=(numeros[mitad:total],el_bloqueo))

# Activación de los hilos 'th1' y 'th2'.

t_activ1 = time.time() # Tiempo de inicio de activación de los hilos.
th1.start()
th2.start()
t_activ2 = time.time() # Tiempo final de activación de los hilos.

print(f"Tiempo de activación:                        {t_activ2 - t_activ1}")

# El hilo principal espera a que terminen los 2 hilos.

t_esp1 = time.time() # Tiempo de inicio de espera de los hilos.
th1.join()
th2.join()
t_esp2 = time.time() # Tiempo final de espera de los hilos
print(f"Tiempo de espera de los hilos                {t_esp2 - t_esp1}")

# tiempo final del programa
T2 = time.time()
print("Nuevamente en el hilo principal")
print(f"La suma total es:                            {suma_total:.8e}")
print(f"Tiempo total:                                {T2 - T1}")
