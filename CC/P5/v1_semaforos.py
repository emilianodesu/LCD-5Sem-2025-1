"""
Versión con semáforos

Equipo 1:

Alan Magno Martínez Muñoz
Carlos Emiliano Mendoza Hernández
Erick Yair Aguilar Martínez
Imanol Mendoza Saenz de Buruaga
Luis Enrique Villalón Pineda
"""
import threading

class SharedData:
    """Contains shared data"""
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.items_produced = 0
        self.items_consumed = 0
        self.computer_data = {
            'top': 0, 'name': '', 'country': '',
            'cores': 0, 'ram': 0, 'storage': 0, 'tflops': 0, 'os': ''
        }
        # Semaphores
        self.s = threading.Semaphore(1) # Binary semaphore for shared resource access
        self.n = threading.Semaphore(0) # To signal writer when an item is produced
        self.e = threading.Semaphore(1) # To signal reader when space is available

class Reader(threading.Thread):
    """Reads user input"""
    def __init__(self, shared_data):
        super().__init__()
        self.shared_data = shared_data

    def run(self):
        while self.shared_data.items_produced < 5:
            self.shared_data.e.acquire()  # Wait for empty space
            with self.shared_data.s:  # Lock shared resources
                # Get input from user
                name = input("\nNombre: ")
                country = input("Pais de origen: ")
                cores = int(input("Cantidad de núcleos: "))
                ram = float(input("Cantidad de RAM (TB): "))
                storage = float(input("Almacenamiento (TB): "))
                tflops = float(input("TeraFLOPS: "))
                os = input("Sistema Operativo: ")

                # Update shared data
                self.shared_data.computer_data['top'] += 1
                self.shared_data.computer_data['name'] = name
                self.shared_data.computer_data['country'] = country
                self.shared_data.computer_data['cores'] = cores
                self.shared_data.computer_data['ram'] = ram
                self.shared_data.computer_data['storage'] = storage
                self.shared_data.computer_data['tflops'] = tflops
                self.shared_data.computer_data['os'] = os
                self.shared_data.items_produced += 1

                # Notify writer that an item is ready
                self.shared_data.n.release()

class Writer(threading.Thread):
    """Writes data to the CSV file"""
    def __init__(self, shared_data):
        super().__init__()
        self.shared_data = shared_data

    def run(self):
        # Initialize the CSV file with headers
        with open(self.shared_data.csv_file, 'w', encoding='utf-8') as file:
            file.write("0,NAME,COUNTRY,CORES,RAM,STORAGE,TFLOPS,OS\n")

        while self.shared_data.items_consumed < 5:
            self.shared_data.n.acquire()  # Wait for an item to be produced
            with self.shared_data.s:  # Lock shared resources
                # Write data to the file
                with open(self.shared_data.csv_file, 'a', encoding='utf-8') as file:
                    whole_thing = f"{self.shared_data.computer_data['top']},"
                    whole_thing += f"{self.shared_data.computer_data['name']},"
                    whole_thing += f"{self.shared_data.computer_data['country']},"
                    whole_thing += f"{self.shared_data.computer_data['cores']},"
                    whole_thing += f"{self.shared_data.computer_data['ram']},"
                    whole_thing += f"{self.shared_data.computer_data['storage']},"
                    whole_thing += f"{self.shared_data.computer_data['tflops']},"
                    whole_thing += f"{self.shared_data.computer_data['os']}\n"
                    file.write(whole_thing)

                # Mark the item as consumed
                self.shared_data.items_consumed += 1

                # Notify reader that space is available
                self.shared_data.e.release()

if __name__ == '__main__':
    sd = SharedData('computersV1.csv')
    reader = Reader(sd)
    writer = Writer(sd)
    reader.start()
    writer.start()
    reader.join()
    writer.join()
    print("Process finished")
