import os
import matplotlib.pyplot as plt
import numpy as np

# Directory containing the BED files
bed_dir = "/home/me1117/cutrun/gene_signatures/H3K27"  

# Define pathway pairs
pathways = ["eff", "il2", "il6", "mem", "tgfb"]
file_pairs = [(f"H3K27_A_{p}_peaks_gene_intersections.bed", f"H3K27_N_{p}_peaks_gene_intersections.bed", p) for p in pathways]

# Define total peaks for normalization
total_peaks_A = 2370
total_peaks_N = 12887

# Function to extract unique gene-peak intersections from a BED file
def extract_genes(file_path):
    genes = set()
    with open(file_path, "r") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 4:
                genes.add(parts[3])  # Gene name is in column 4
    return genes

# Store normalized values
normalized_counts_A = []
normalized_counts_N = []
normalized_counts_common = []
labels = []

# Process each pathway
for file_A, file_N, pathway in file_pairs:
    path_A = os.path.join(bed_dir, file_A)
    path_N = os.path.join(bed_dir, file_N)
    
    if os.path.exists(path_A) and os.path.exists(path_N):
        genes_A = extract_genes(path_A)
        genes_N = extract_genes(path_N)
        
        common_genes = genes_A & genes_N  # Find common genes
        unique_A = genes_A - common_genes  # Subtract common from A
        unique_N = genes_N - common_genes  # Subtract common from N

        count_A = len(unique_A) / total_peaks_A  # Normalize by total peaks in A
        count_N = len(unique_N) / total_peaks_N  # Normalize by total peaks in N
        count_common = len(common_genes) / ((total_peaks_A + total_peaks_N) / 2)  # Normalize by avg peaks

        normalized_counts_A.append(count_A)
        normalized_counts_N.append(count_N)
        normalized_counts_common.append(count_common)
        labels.append(pathway)  # Pathway name for x-axis

    else:
        print(f"Skipping {file_A} vs {file_N}: One or both files are missing.")

# Plot the normalized counts
x = np.arange(len(labels))  # X-axis positions

plt.figure(figsize=(8, 5))
bar_width = 0.3

plt.bar(x - bar_width, normalized_counts_A, width=bar_width, label="H3K27_A (Unique)", color="blue", alpha=0.7)
plt.bar(x, normalized_counts_N, width=bar_width, label="H3K27_N (Unique)", color="red", alpha=0.7)
plt.bar(x + bar_width, normalized_counts_common, width=bar_width, label="Common", color="green", alpha=0.7)

plt.xticks(x, labels)  # Add pathway names on x-axis
plt.xlabel("Pathways")
plt.ylabel("Normalized Gene-Peak Intersections")
plt.title("Normalized Unique Gene-Peak Intersections in H3K27_A vs H3K27_N")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.6)

# Save plot
plt.savefig("normalized_gene_peak_intersections_unique_H3K27.png", dpi=300)
plt.show()