"""TRES PROCESOS REALIZAN DIFERENTES OPERACIONES"""

# Ejecute en Linux o MAC: mpirun -n 3 python3 mpi_3.py
# Ejecute en Windows: mpiexec -n 3 python mpi_3.py

##### MÓDULOS #####

from mpi4py import MPI


##### INICIO #####

# Identificador de procesos.
rank = MPI.COMM_WORLD.Get_rank()

# Variables
A = 6.0
B = 3.0

# Proceso 0.
if rank == 0:
    print(f"Proceso {rank} Suma: {A + B}")

# Proceso 1.
if rank == 1:
    print(f"Proceso {rank} Multiplicacion: {A * B}")

# Proceso 2.
if rank == 2:
    print(f"Proceso {rank} Maximo: {max(A,B)}")
