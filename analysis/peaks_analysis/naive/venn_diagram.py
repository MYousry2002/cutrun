import pandas as pd
from venn import venn
import matplotlib.pyplot as plt
import os

# Define the target directory
target_directory = "../../../analysis/naive/"

# Change to the target directory
os.chdir(target_directory)

# Print the current directory to confirm the change
print("Current directory:", os.getcwd())

# Load the binary matrix
binary_matrix = pd.read_csv("binary_matrix.csv")

# Prepare the sets for the Venn diagram
sets = {
    "nH3K4_A": set(binary_matrix.index[binary_matrix['nH3K4_A'] == 1]),
    "nH3K4_N": set(binary_matrix.index[binary_matrix['nH3K4_N'] == 1]),
    "nH3K27_A": set(binary_matrix.index[binary_matrix['nH3K27_A'] == 1]),
    "nH3K27_N": set(binary_matrix.index[binary_matrix['nH3K27_N'] == 1]),
}

# Generate the Venn diagram
plt.figure(figsize=(10, 10))
venn(sets)

# Add title and save the plot
plt.title("Venn Diagram of H3K4/H3K27 Adults/Neonates Intersections")
output_file = "venn_diagram_new.png"
plt.savefig(output_file, dpi=300)
plt.show()

print(f"Venn diagram saved as {output_file} in the current directory.")