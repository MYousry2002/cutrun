import pandas as pd
import os

# Define the target directory
target_directory = "../../../analysis/naive/"

# Change to the target directory
os.chdir(target_directory)

# Print the current directory to confirm the change
print("Current directory:", os.getcwd())

# Load the multiinter_output.bed file
data = pd.read_csv(
    "multiinter_output.bed",
    sep="\t",
    header=None,
    names=["chrom", "start", "end", "count", "list", "nH3K4_A", "nH3K4_N", "nH3K27_A", "nH3K27_N"]
)

# Define file names (column headers)
files = ["nH3K4_A", "nH3K4_N", "nH3K27_A", "nH3K27_N"]

# Initialize a binary matrix using the existing columns
binary_matrix = data[files].copy()

# Convert the "list" column to reflect presence/absence in the binary matrix
for idx, file_list in enumerate(data['list']):
    for file_idx in str(file_list).split(','):
        binary_matrix.iloc[idx, int(file_idx) - 1] = 1  # Set presence to 1

# Save the binary matrix to a CSV file
binary_matrix.to_csv("binary_matrix.csv", index=False)

print("Binary matrix saved to binary_matrix.csv.")