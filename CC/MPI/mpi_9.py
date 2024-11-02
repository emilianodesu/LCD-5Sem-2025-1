"""LAS FUNCIONES DE ENVÍO 'Isend' Y de RECEPCIÓN 'Irecv' DE LOS PROCESOS 0 Y 1 SON NO BLOQUEANTES
SIN EMBARGO LOS PROCESOS SE BLOQUEAN CON 'Wait' CUANDO ESTÁN RECIBIENDO UN MENSAJE
EN ESTA OCASIÓN HAY UNA OPERACIÓN DE DIVISIÓN ANTES DE QUE EL PROCESO 1 RECIBA UN 
MENSAJE DEL PROCESO 0"""

# Ejecute en Linux o MAC: mpirun -n 2 python3 mpi_9.py
# Ejecute en Windows: mpiexec -n 2 python mpi_9.py

##### MÓDULOS #####

import numpy # Manejo de arreglos y cómputo científico.
from mpi4py import MPI

##### INICIO #####

# Objeto tipo comunicador.
comm = MPI.COMM_WORLD

# Id. de procesos.
rank = comm.Get_rank()

# Reserva memoria para un arreglo de un solo número aleatorio.
randNum = numpy.zeros(1)
diffNum = numpy.zeros(1)

# El proceso 1 envía un dato al proceso 0.
if rank == 1:
    # diffNum es un número aleatorio.
    diffNum = numpy.random.random_sample(1)
    # Un número aleatorio.
    randNum = numpy.random.random_sample(1)
    # Imprime el número del proceso y el núemero aleatorio 'randNum'.
    print("Proceso", rank, "enviara el numero", randNum[0])
    # Envía el mensaje al proceso 0.
    # La función 'Isend' es no bloqueante.
    comm.Isend(randNum, dest=0)
    # Imprime el número que envió sin esperar a que el
	# proceso 0 reciba el mensaje.
    print("Proceso", rank, "envio el numero", randNum[0])
    # Sin esperar a que el proceso 0 reciba el mensaje
    # el proceso 1 divide diffNum entre 3.14.
    diffNum /= 3.14
    # Imprime la división.
    print("Sin esperar, el proceso 1 realiza la division:  diffNum = ", diffNum[0])
    # La función 'Irecv' es no bloqueante.
    req = comm.Irecv(randNum, source=0)
    # Bloquea hasta que se haya recibido el mensaje del proceso 0.
    # Esto es necesario antes de que se imprima el valor 'randNum'.
    req.Wait()
    # Imprime el mensaje que recibió.
    print("Proceso", rank, "recibio el numero", randNum[0])

# El proceso 0 recibe un dato del proceso 1.
if rank == 0:
    print("Proceso", rank, "esperando un mensaje")
    # Recibe el mensaje del proceso 1.
    req = comm.Irecv(randNum, source=1)
    # Bloquea el receptor hasta que se haya recibido el mensaje.
    # Esto es necesario antes de que el proceso imprima 'randNum' y lo multiplique por 2.
    req.Wait()
    # Imprime el mensaje.
    print("Proceso", rank, "recibio el numero", randNum[0])
    # Multiplica por 2 el número que recibió.
    randNum *= 2
    # Envía el mensaje al proceso 1.
    # La función 'Isend' es no bloqueante.
    comm.Isend(randNum, dest=1)
