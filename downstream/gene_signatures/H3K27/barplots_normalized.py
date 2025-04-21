import os
import matplotlib.pyplot as plt
import numpy as np

# Directory containing the BED files
bed_dir = "/home/me1117/cutrun/downstream/gene_signatures/H3K27"

# Pathway names used in the file suffixes
pathways = [
    "effector_vs_memory_cd8_up",
    "il2_stat5_signaling",
    "il6_jak_stat3_signaling",
    "effector_vs_memory_cd8_dn",
    "tgf_beta_signaling",
    "housekeeping",
    "methionine"
]

# Build file name tuples using new suffix
file_pairs = [
    (
        f"H3K27_A_{p}_peaks_gene_intersections.bed",
        f"H3K27_N_{p}_peaks_gene_intersections.bed",
        p
    ) for p in pathways
]

# Total peaks per condition
total_peaks_A = 2370
total_peaks_N = 12887

# Store results
proportions_A = []
proportions_N = []
labels = []

for file_A, file_N, label in file_pairs:
    path_A = os.path.join(bed_dir, file_A)
    path_N = os.path.join(bed_dir, file_N)

    if os.path.exists(path_A) and os.path.exists(path_N):
        num_genes_A = sum(1 for _ in open(path_A))
        num_genes_N = sum(1 for _ in open(path_N))

        prop_A = num_genes_A / total_peaks_A
        prop_N = num_genes_N / total_peaks_N

        proportions_A.append(prop_A)
        proportions_N.append(prop_N)
        labels.append(label.replace("_", "\n"))  # Pretty x-axis formatting
    else:
        print(f"Skipping {file_A} vs {file_N} — missing file.")

# Plotting
x = np.arange(len(labels))
bar_width = 0.35

plt.figure(figsize=(10, 6))
plt.bar(x - bar_width / 2, proportions_A, width=bar_width, label="H3K27_A", color="blue", alpha=0.7)
plt.bar(x + bar_width / 2, proportions_N, width=bar_width, label="H3K27_N", color="red", alpha=0.7)

plt.xticks(x, labels)
plt.xlabel("Pathways")
plt.ylabel("Proportion of Genes with Peaks")
plt.title("Proportional Enrichment of H3K27me3 Peaks by Pathway (Gene-Centered)")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig("proportional_genes_with_peaks_H3K27.png", dpi=300)
plt.show()