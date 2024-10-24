##### TRES PROCESOS REALIZAN DIFERENTES OPERACIONES #####

# Ejecute en Linux o MAC: mpirun -n 3 python3 MPI03.py
# Ejecute en Windows: mpiexec -n 3 python3 MPI03.py


##### MÓDULOS #####

from mpi4py import MPI


##### INICIO #####

# Identificador de procesos.
rank = MPI.COMM_WORLD.Get_rank()

# Variables 
a = 6.0
b = 3.0

# Proceso 0.
if rank == 0:
        print(f"Proceso {rank} Suma: {a + b}")

# Proceso 1.
if rank == 1:
        print(f"Proceso {rank} Multiplicación: {a * b}")

# Proceso 2.
if rank == 2:
        print(f"Proceso {rank} Máximo: {max(a,b)}")
