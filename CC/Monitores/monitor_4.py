"""PRODUCTOR/CONSUMIDOR USANDO UNA LISTA Y UNA CONDICIÓN"""

##### MÓDULOS #####
from threading import Thread, Condition
import time

##### VARIABLES GLOBALES #####

# Lista como buffer circular.
buffer = []
# Tamaño del buffer.
MAX_NUM = 10
# Objeto condición.
condition = Condition()

##### CLASES PRODUCTOR Y CONSUMIDOR #####
# Clase Productor.

class Productor(Thread):
    """Clase Productor."""
    def run(self):
        # Variables
        num = 0  # Dato producido.
        global buffer
        retardo = 0.5
        while True:
            # Entra al monitor
            condition.acquire()
            # Verifica si el buffer está lleno.
            if len(buffer) == MAX_NUM:
                print("Buffer lleno, Productor esperando")

                retardo = retardo + 1
                # Espera que el comsumidor consuma un dato.
                condition.wait()
                print ("Espacio en el buffer, el consumidor notificó al Productor")

            # Agrega un dato al buffer, al final del dato anterior.
            buffer.append(num)
            print ("Dato producido", num)

            # Notifica que se agregó un dato al buffer.
            condition.notify()

            # Sale del monitor.
            condition.release()
            # Duerme.
            time.sleep(retardo)
            num = num + 1
# Clase Consumidor.

class Consumidor(Thread):
    """Clase Consumidor."""
    def run(self):
        # Variables
        global buffer
        retardo = 1
        while True:
            # Entra al monitor.
            condition.acquire()

            # Verifica si el buffer está vacío.
            if not buffer:
                print("Buffer vacío, Consumidor esperando")
                # Espera que el Productor agregue más datos.
                condition.wait()
                print("El Productor agregó un dato al buffer y lo notificó al Consumidor")

            # Saca el primer dato y lo borra del buffer.
            num = buffer.pop(0)
            print("Dato consumido", num)
            # Notifica que se sacó un dato del buffer.
            condition.notify()
            # Sale del monitor.
            condition.release()
            # Duerme.
            time.sleep(retardo)


##### INICIO #####
Productor().start()
Consumidor().start()
