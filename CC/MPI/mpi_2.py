"""ENVÍA UN MENSAJE, send Y recv SE BLOQUEAN HASTA QUE SE RECIBA EL MENSAJE"""

# Ejecute en Windows: mpiexec -n 2 python mpi_2.py
# Ejecute en Linux o MAC: mpirun -n 2 python3 mpi_2.py
##### MÓDULOS #####

from mpi4py import MPI # MPI para Python.


##### INICIO #####

# Objeto tipo comunicador.
comm = MPI.COMM_WORLD

# Obtiene el identificador de los procesos.
rank = comm.Get_rank()

# Para el proceso 0
if rank == 0:
    # Crea el diccionario 'data'.
    data = {'a': 7, 'b': 3.14}
    # Envía el mensaje 'data' al proceso 1.
    # La función se bloquea hasta que se reciba el mensaje.
    comm.send(data, dest=1)

# Para el proceso 1
elif rank == 1:
    # Recibe el mensaje desde el proceso 0 y lo coloca en 'dato'.
    dato = comm.recv(source=0)
    # Imprime el mensaje 'dato'.
    print('On process 1, data is ',dato)
