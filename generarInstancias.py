import os
import random

def generate_instance(directory, filename, dimension):
    # Generar una matriz completa aleatoria de pesos de aristas con elementos diagonales establecidos en 0
    edge_weights = [[0 if i == j else random.randint(1, 100) for j in range(dimension)] for i in range(dimension)]

    # Preparar la cadena de la instancia
    instance_str = f"NAME: {filename}\n"
    instance_str += "TYPE: ATSP\n"
    instance_str += f"DIMENSION: {dimension}\n"
    instance_str += "EDGE_WEIGHT_TYPE: EXPLICIT\n"
    instance_str += "EDGE_WEIGHT_FORMAT: FULL_MATRIX\n"
    instance_str += "EDGE_WEIGHT_SECTION:\n"

    for row in edge_weights:
        instance_str += " ".join(map(str, row)) + "\n"

    instance_str += "EOF"

    # Crear el directorio "instances" si no existe
    os.makedirs(directory, exist_ok=True)

    # Construir la ruta completa al archivo
    file_path = os.path.join(directory, filename)

    # Escribir la instancia en el archivo especificado
    with open(file_path, "w") as file:
        file.write(instance_str)

    print(f"Instancia guardada en: {file_path}")

# Ejemplo: Generar una instancia con dimensión 8 y guardarla en el directorio "instances"
directory = "instances"
filename = input("Ingrese el nombre del archivo a crear (por ejemplo, atsp8_1.tsp): ")
dimension = int(input("Ingrese la dimensión: "))
generate_instance(directory, filename, dimension)
