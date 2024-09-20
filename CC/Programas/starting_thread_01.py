"""
CREA UN HILO QUE INVOCA A UNA FUNCIÓN #####
EL HILO PRINCIPAL SIGUE SU CURSO A MENOS QUE SE DETENGA CON ######
EL METODO 'join'
"""

# 'logging': Implementa un registro de eventos para aplicaciones y bibliotecas.
# puede incluir mensajes propios integrados con mensajes de módulos de terceros.
import logging

import threading # Concurrencia basada en hilos.
import time # Acceso al tiempo y conversiones.


##### Función #####
def thread_function(name):
    """Imprime el mensaje configurado por 'logging.basicConfig' (la hora en formato H:M:S),
    la cadena Thread seguida del valor del argumento 'name' (1)."""
    logging.info("Thread %s: starting", name)

    # Imprime el número de hilos activos
    logging.info("Thread %s: Num hilos al inicio de la función %d", name, threading.active_count())

    # Duerme 5 segundos
    time.sleep(5)

    # Antes de terminar la función imprime la cadena Thread seguida del valor del argumento 'name'
    logging.info("Thread %s: finishing", name)

    # Número  de objetos 'Thread' al final del programa.
    logging.info("Main    : Número de hilos al final de la función %d", threading.active_count())


##### Main #####

if __name__ == "__main__":  # Permite que este archivo se pueda importar como módulo sin ejecutar
                            # las lineas que se encuentran debajo.

    # Formato del tiempo que se imprime
    FORMAT = "%(asctime)s: %(message)s"
    logging.basicConfig(format=FORMAT, level=logging.INFO,
                        datefmt="%H:%M:%S")

    # Número  de objetos 'Thread' actuales.
    NUMERO_HILOS = threading.active_count()
    logging.info("Main    : Número de hilos al inicio %d", NUMERO_HILOS)

    # Impresión antes de que se cree el hilo.
    logging.info("Main    : before creating thread")

    # Construye 'x' como objeto 'Thread'.
    # El hilo ejecutará la función 'thread_function' con argumento '1'.
    x = threading.Thread(target=thread_function, args=(1,))

    # Imprime una cadena antes de iniciar la actividadd  del hilo.
    logging.info("Main    : before running thread")

    # Inicia la actividad del hilo 'x'.
    # En este momento ya tenemos 2 hilos activos.
    x.start()

    # Imprime una cadena antes de que termine la actividad del hilo.
    logging.info("Main    : wait for the thread to finish")

    # El hilo principal espera hasta que el hilo 'x' finalice.
    x.join()

    # Número  de objetos 'Thread' al final del programa.
    logging.info("Main    : Número de hilos al final %d", threading.active_count())

    # Imprime una cadena desde el hilo principal.
    logging.info("Main    : all done")
