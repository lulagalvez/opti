from dfj import dfj
from gg import gg
from mtz import mtz
import os

def list_instances():
    instance_files = [f for f in os.listdir("instances/") if os.path.isfile(os.path.join("instances/", f))]
    print("Instancias disponibles:")
    for i, file_name in enumerate(instance_files, start=1):
        print(f"{i}. {file_name}")
    return instance_files

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    matrix_started = False
    matrix = []

    for line in lines:
        if line.startswith("EDGE_WEIGHT_SECTION"):
            matrix_started = True
            continue
        if matrix_started and line.strip() == "EOF":
            break
        if matrix_started:
            row = [int(num) for num in line.split()]
            matrix.append(row)

    return matrix

def main():
    print("Elegir algoritmo:")
    print("1. DFJ (Dantzig-Fulkerson-Johnson)")
    print("2. GG (Gilmore-Gomory)")
    print("3. MTZ (Miller-Tucker-Zemlin)")

    algorithm_choice = input("Elegir el numero de algoritmo a ejecutar: ")

    if algorithm_choice == "1":
        algorithm_name = "DFJ"
        solve_atsp = dfj
    elif algorithm_choice == "2":
        algorithm_name = "GG"
        solve_atsp = gg
    elif algorithm_choice == "3":
        algorithm_name = "MTZ"
        solve_atsp = mtz
    else:
        print("Error.")
        return

    print(f"Seleccionado algoritmo de {algorithm_name}.")

    instance_files = list_instances()
    if not instance_files:
        print("No se encontraron instancias.")
        return

    file_choice = input("Ingresar numero de instancia: ")
    try:
        file_index = int(file_choice) - 1
        selected_file = instance_files[file_index]
    except (ValueError, IndexError):
        print("Numero invalido.")
        return

    file_path = os.path.join("instances", selected_file)

    distance_matrix = read_file(file_path)
    solution = solve_atsp(distance_matrix)

if __name__ == "__main__":
    main()
