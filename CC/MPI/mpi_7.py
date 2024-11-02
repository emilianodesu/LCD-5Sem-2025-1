"""UN PROCESO ENVÍA UN DATO A OTRO, SE USAN LAS FUNCIONES 'Isend' Y 'Irecv' NO BLOQUEANTES
LA FUNCIÓN 'Wait' INMEDIATAMENTE DESPUÉS DE LAS FUNCIONES 'Isend' Y 'Irecv' BLOQUEA EL PROCESO
HASTA QUE LA OPERACIÓN DE ENVÍO Y RECEPCIÓN SE HAYAN COMPLETADO."""

# Ejecute en Linux o MAC: mpirun -n 2 python3 mpi_7.py
# Ejecute en Windows: mpiexec -n 2 python mpi_7.py


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

# El proceso 1 envía un dato al proceso 0.
if rank == 1:
    # Un número aleatorio.
    randNum = numpy.random.random_sample(1)
    # Imprime el número del proceso y el núemero aleatorio.
    print("Proceso", rank, "enviara el numero", randNum[0])
    # Envía el mensaje al proceso 0.
    # La funcióm 'Isend' es no bloqueante.
    req = comm.Isend(randNum, dest=0)
    # Bloquea el emisor hasta que se haya recibido el mensaje.
    req.Wait()
    # Imprime el número que envió.
    print("Proceso", rank, "envio el numero", randNum[0])

# El proceso 0 recibe un dato del proceso 1.
if rank == 0:

    print("Proceso", rank, "esperando un mensaje")
    # Recibe el mensaje del proceso 1.
    # En numpy usa usa 'Irecv' en lugar de 'irecv'.
    req = comm.Irecv(randNum, source=1)
    # Bloquea el receptor hasta que se haya recibido el mensaje.
    # Comentar 'req.Wait' y volver a correr para observar
    # el comportamiento del destino no bloqueante.
    req.Wait()
    # Imprime el mensaje.
    print("Proceso", rank, "recibio el numero", randNum[0])
