"""DOS PROCESOS ENVÍAN Y RECIBEN MENSAJES UNO AL OTRO,
LAS FUNCIONES Send Y Recv SE BLOQUEAN HASTA QUE LLEGAN LOS MENSAJES"""

# Ejecute en Linux o MAC: mpirun -n 2 python3 mpi_5.py
# Ejecute en Windows: mpiexec -n 2 python mpi_5.py

##### MÓDULOS #####

import time
import numpy # Manejo de arreglos y cómputo científico.
from mpi4py import MPI


##### INICIO #####
# Objeto tipo comunicador.
comm = MPI.COMM_WORLD

# Id. de procesos.
rank = comm.Get_rank()

# Reserva memoria para un arreglo de un solo número aleatorio.
randNum = numpy.zeros(1)

# El proceso 1 envía y recibe mensajes del proceso 0.
if rank == 1:
    # Un número aleatorio.
    randNum = numpy.random.random_sample(1)
    # Imprime el número del proceso y el núemero aleatorio.
    print("Proceso", rank, "enviara el numero", randNum[0])
    # Espera unos segundos antes de enviar el mensaje.
    time.sleep(5)
    # Envía el mensaje al proceso 0.
    # En numpy se usa 'Send' en lugar de 'send'.
    comm.Send(randNum, dest=0)
    # Imprime el número que envió.
    print("Proceso", rank, "envio el numero", randNum[0])
    # Recibe un mensaje del proceso 0.
    comm.Recv(randNum, source=0)
    # Imprime el número que recibió.
    print("Proceso", rank, "recibio el numero", randNum[0])

# El proceso 0 recibe y envía un mensaje al proceso 1.
if rank == 0:
    print("Proceso", rank, "esperando un mensaje")
    # Recibe el mensaje del proceso 1.
    # En numpy usa usa 'Recv' en lugar de 'recv'.
    comm.Recv(randNum, source=1)
    # Imprime el mensaje.
    print("Proceso", rank, "recibio el numero", randNum[0])
    # Multiplica por 2 el mensaje.
    randNum *= 2
    # Espera unos segundos antes de enviar el mensaje.
    time.sleep(7)
    # Envía al proceso 1 el mensaje multiplicado por 2.
    comm.Send(randNum, dest=1)
    # Imprime el número que envió.
    print("Proceso", rank, "envio el numero", randNum[0])
