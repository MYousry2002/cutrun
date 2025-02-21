import pandas as pd
from upsetplot import UpSet, from_memberships
import matplotlib.pyplot as plt
import os

# Define the target directory
target_directory = "../../../analysis/activated/"

# Change to the target directory
os.chdir(target_directory)

# Print the current directory to confirm the change
print("Current directory:", os.getcwd())

# Load the binary matrix
binary_matrix = pd.read_csv("binary_matrix.csv")

# Check the binary matrix structure
print("Binary Matrix Head:\n", binary_matrix.head())

# Prepare data for UpSet plot using `from_memberships`
binary_matrix.columns = ['H3K4_A', 'H3K4_N', 'H3K27_A', 'H3K27_N']
memberships = binary_matrix.apply(lambda row: list(binary_matrix.columns[row == 1]), axis=1)
data = from_memberships(memberships)

# Print the processed data for debugging
print("\nProcessed Data for UpSet:\n", data)

# Create the UpSet plot
upset = UpSet(data, subset_size='count', show_counts=True)
fig = plt.figure(figsize=(12, 8))
upset.plot(fig=fig)

# Save the plot
output_file = "upset_plot.png"
plt.savefig(output_file, dpi=300)
plt.close()

print(f"Corrected UpSet plot saved as {output_file} in the current directory.")