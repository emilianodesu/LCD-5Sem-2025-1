"""
Versión con MPI

Equipo 1:

Alan Magno Martínez Muñoz
Carlos Emiliano Mendoza Hernández
Erick Yair Aguilar Martínez
Imanol Mendoza Saenz de Buruaga
Luis Enrique Villalón Pineda
"""

# Ejecute en Linux o MAC: mpirun -n 2 python3 v3_mpi.py
# Ejecute en Windows: mpiexec -n 2 python v3_mpi.py

# Modulo MPI
from mpi4py import MPI

# Objeto tipo comunicador.
comm = MPI.COMM_WORLD
# Id. de procesos.
rank = comm.Get_rank()

# Variables para contar los elementos producidos y consumidos.
items_produced = 0
items_consumed = 0

# Proceso 0
if rank == 0:
    # Mientras no se hayan producido 5 elementos.
    file_name = input("\nNombre del archivo: ")
    comm.send(file_name, dest=1)
    while items_produced < 5:
        name = input("\nNombre: ")
        country = input("Pais de origen: ")
        cores = int(input("Cantidad de núcleos: "))
        ram = float(input("Cantidad de RAM (TB): "))
        storage = float(input("Almacenamiento (TB): "))
        tflops = float(input("TeraFLOPS: "))
        os = input("Sistema Operativo: ")
        # Enviar los datos al proceso 1
        data = (name, country, cores, ram, storage, tflops, os)
        comm.send(data, dest=1)
        items_produced += 1
        # Esperar a que el proceso 1 haya consumido los datos
        comm.recv(source=1)

# Proceso 1
if rank == 1:
    file_name = comm.recv(source=0)
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write("0,NAME,COUNTRY,CORES,RAM,STORAGE,TFLOPS,OS\n")
    # Mientras no se hayan consumido 5 elementos.
    while items_consumed < 5:
        # Recibir los datos del proceso 0
        data = comm.recv(source=0)
        # Escribir los datos en el archivo
        with open(file_name, 'a', encoding='utf-8') as file:
            whole_thing = f"{items_consumed + 1},{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]}\n"
            file.write(whole_thing)
        print(f"\nComputadora Top {items_consumed+1} guardado en {file_name}")
        items_consumed += 1
        # Notificar al proceso 0 que se ha consumido un elemento
        comm.send(None, dest=0)
