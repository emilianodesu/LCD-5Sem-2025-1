##### LAS FUNCIONES DE ENVÍO 'Isend' Y RECEPCIÓN 'Irecv' DE LOS PROCESOS 0 Y 1 SON NO BLOQUEANTES   #####
##### SIN EMBARGO LOS PROCESOS SE BLOQUEAN CON 'Wait' CUANDO ESTÁN RECIBIENDO UN MENSAJE            ##### 

# Ejecute en Linux o MAC: mpirun -n 2 python3 MPI08.py
# Ejecute en Windows: mpiexec -n 2 python3 MPI08.py


##### MÓDULOS #####

import numpy # Manejo de arreglos y cómputo científico.
from mpi4py import MPI
import time


##### INICIO #####

# Objeto tipo comunicador.
comm = MPI.COMM_WORLD

# Id. de procesos.
rank = comm.Get_rank()

# Reserva memoria para un arreglo de un solo número aleatorio.
# Cuando se usa numpy se debe declarar un buffer (en este caso llamado 'randNum') antes de usarlo.
randNum = numpy.zeros(1)

# El proceso 1 envía un dato al proceso 0.
if rank == 1:

        # Un número aleatorio.
        randNum = numpy.random.random_sample(1)

        # Imprime el número del proceso y el núemero aleatorio.
        print("Proceso", rank, "enviará el número", randNum[0])

        # Envía el mensaje al proceso 0.
        # La función 'Isend' es no bloqueante.
        comm.Isend(randNum, dest=0)

        # Imprime el número que envió. OBSERVAR que a diferencia del ejemplo anterior
		# no hay un 'Wait' despues de enviar el mensaje por lo que imprime la siguiente cadena
		# sin esperar a que el receptor haya recibido dicho mensaje. 
        print("Proceso", rank, "envió el número", randNum[0])

        # La función 'Irecv' es no bloqueante.
        req = comm.Irecv(randNum, source=0)
 
        # Bloquea hasta que se haya recibido el mensaje del proceso 0.
        # Esto es necesario antes de que se imprima el valor 'randNum'.
        req.Wait()

        # Imprime el mensaje que recibió.
        print("Proceso", rank, "recibió el número", randNum[0])
        

# El proceso 0 recibe un dato del proceso 1.
if rank == 0:

        print("Proceso", rank, "esperando un mensaje")
        
        # Recibe el mensaje del proceso 1.
        # En numpy usa usa 'Recv' en lugar de 'recv'.
        req = comm.Irecv(randNum, source=1)

        # Bloquea el receptor hasta que se haya recibido el mensaje.
        # Esto es necesario antes de que el proceso imprima 'randNum' y lo multiplique por 2.
        req.Wait()

        # Imprime el mensaje.
        print("Proceso", rank, "recibió el número", randNum[0])

        # Multiplica por 2 el número que recibió.
        randNum *= 2

        # Envía el mensaje al proceso 1.
        # La función 'Isend' es no bloqueante.
        comm.Isend(randNum, dest=1)
