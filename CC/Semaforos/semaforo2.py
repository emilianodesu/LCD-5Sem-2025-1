##### PRODUCTOR/CONSUMIDOR CON SEMAFOROS #####


##### MÓDULOS #####

import threading
import time


##### VARIABLES GLOBALES #####

# Variables compartidas.

CAPACITY = 10                           # Tamaño del buffer
buffer = [0 for i in range(CAPACITY)]   # Rellena el buffer con ceros.
in_index = 0                    # Lleva el índice de la posición en el buffer del nuevo dato del productor.
out_index = 0                   # Lleva el índice de la posición en el buffer del dato a consumir en el consumidor.
 
# Declación de semáforos.

# Semáforo s. Permite que solo el productor o el consumidor pueda modificar el buffer.
s = threading.Semaphore(1)

# Semáforo e. Bloquea cuando en el buffer ya no hay espacios para más datos.
e = threading.Semaphore(CAPACITY)

# Semáforo n. Bloquea cuando no hay datos en el buffer.
n = threading.Semaphore(0)           


##### DEFINICIÓN DE LAS CLASES PRODUCTOR Y CONSUMIDOR #####

 
# Clase productor

# Por default crea un objeto tipo 'Thread'
class Producer(threading.Thread):
  def run(self):
     
    global CAPACITY, buffer, in_index
    global s, e, n
     
    items_produced = 0 # Lleva el conteo de los datos producidos.
    counter = 0        # Este es el dato producido.
     
    while items_produced < 20:

      # Produce un dato
      counter += 1

      e.acquire()   # Decrementa el semáforo 'e', mencionando que se produjo un nuevo dato.
      s.acquire()   # Solicita entrar a la sección crítica.

      # Inicia SC.

      print(f"       Productor: Valor del semáforo 'e' {e._value}")
      print(f"       Productor: Valor del semáforo 's' {s._value}")
      print(f"       Productor: Valor del semáforo 'n' {n._value}")
      
      buffer[in_index] = counter
      in_index = (in_index + 1)%CAPACITY
      print("Dato producido : ", counter)

      # Finaliza SC.

      s.release()   # Libera la sección crítica.
      n.release()   # Incrementa el semáforo 'n', mencioanndo que ya hay datos en el buffer.
       
      time.sleep(1)
       
      items_produced += 1

 
# Clase consumidor

class Consumer(threading.Thread):
  def run(self):
     
    global CAPACITY, buffer, out_index
    global s, e, n
     
    items_consumed = 0 # Lleva el conteo de los datos consumidos.
     
    while items_consumed < 20:
        
      n.acquire()  # Decrementa el semáforo 'n', verificando que el buffer no esté vacío.
      s.acquire()  # Solicita entrar a la sección crítica.

      # Inicia SC.

      print(f"       Consumidor: Valor del semáforo 'e' {e._value}")
      print(f"       Consumidor: Valor del semáforo 's' {s._value}")
      print(f"       Consumidor: Valor del semáforo 'n' {n._value}")     

      item = buffer[out_index]  # Dato consumido.
      out_index = (out_index + 1)%CAPACITY
      print("Dato consumido : ", item)
      
     # Finaliza SC.
     
      s.release()   # Libera la sección crítica.
      e.release()   # Incrementa el semáforo 'e', mencionando que ya un nuevo espacio disponible en el buffer.
       
      time.sleep(2.5)
       
      items_consumed += 1


##### INICIO #####

# Creating Threads
producer = Producer()
consumer = Consumer()
 
# Starting Threads
consumer.start()
producer.start()
 
# Waiting for threads to complete
producer.join()
consumer.join()
