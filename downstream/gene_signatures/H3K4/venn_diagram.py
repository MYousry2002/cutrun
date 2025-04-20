import os
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Directory containing the BED files
bed_dir = "/home/me1117/cutrun/downstream/gene_signatures/H3K4"

# Define pathway pairs
pathways = ["eff", "il2", "il6", "mem", "tgfb", "housekeeping", "methionine"]
file_pairs = [(f"H3K4_A_{p}_peaks_gene_intersections.bed", f"H3K4_N_{p}_peaks_gene_intersections.bed", p) for p in pathways]

# Function to extract gene names from the 4th column of a BED file
def extract_genes(file_path):
    genes = set()
    with open(file_path, "r") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 4:
                genes.add(parts[3])  # Gene name is in column 4
    return genes

# Generate Venn diagrams for each pathway
for file_A, file_N, pathway in file_pairs:
    path_A = os.path.join(bed_dir, file_A)
    path_N = os.path.join(bed_dir, file_N)
    
    if os.path.exists(path_A) and os.path.exists(path_N):
        genes_A = extract_genes(path_A)
        genes_N = extract_genes(path_N)

        plt.figure(figsize=(5, 5))
        venn2([genes_A, genes_N], set_labels=(f"A_{pathway}", f"N_{pathway}"))  # Shortened labels
        plt.title(f"H3K4_A vs H3K4_N ({pathway})")
        
        # Save file with short name
        plot_filename = f"venn_{pathway}.png"
        plt.savefig(plot_filename, dpi=300)
        plt.show()
        
        print(f"Saved: {plot_filename}")

    else:
        print(f"Skipping {file_A} vs {file_N}: One or both files are missing.")