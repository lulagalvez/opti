import os
import random

def generate_instance(directory, filename, dimension):
    # Generate a random full matrix of edge weights with diagonal elements set to 0
    edge_weights = [[0 if i == j else random.randint(1, 100) for j in range(dimension)] for i in range(dimension)]

    # Prepare the instance string
    instance_str = f"NAME: {filename}\n"
    instance_str += "TYPE: ATSP\n"
    instance_str += f"DIMENSION: {dimension}\n"
    instance_str += "EDGE_WEIGHT_TYPE: EXPLICIT\n"
    instance_str += "EDGE_WEIGHT_FORMAT: FULL_MATRIX\n"
    instance_str += "EDGE_WEIGHT_SECTION:\n"

    for row in edge_weights:
        instance_str += " ".join(map(str, row)) + "\n"

    instance_str += "EOF"

    # Create the "instances" directory if it does not exist
    os.makedirs(directory, exist_ok=True)

    # Construct the full path to the file
    file_path = os.path.join(directory, filename)

    # Write the instance to the specified file
    with open(file_path, "w") as file:
        file.write(instance_str)

    print(f"Instance saved to: {file_path}")

# Example: Generate an instance with dimension 8 and save to "instances" directory
directory = "instances"
filename = input("Enter the name of the file to create (e.g., atsp8_1.tsp): ")
dimension = int(input("Enter the dimension: "))
generate_instance(directory, filename, dimension)
