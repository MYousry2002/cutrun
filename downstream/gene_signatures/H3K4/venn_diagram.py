import os
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Directory with intersected peak files (corrected logic: peaks intersecting gene sets)
bed_dir = "/home/me1117/cutrun/downstream/gene_signatures/H3K4"

# Updated pathway names to match corrected file naming
pathways = [
    "effector_vs_memory_cd8_up",
    "il2_stat5_signaling",
    "il6_jak_stat3_signaling",
    "effector_vs_memory_cd8_dn",
    "tgf_beta_signaling",
    "housekeeping",
    "methionine"
]

# Function to extract unique peak coordinates from intersected BED file
def extract_peaks(file_path):
    peaks = set()
    with open(file_path, "r") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 3:
                # Use (chr, start, end) as unique peak identifier
                peak_id = f"{parts[0]}:{parts[1]}-{parts[2]}"
                peaks.add(peak_id)
    return peaks

# Create Venn diagrams for each pathway
for pathway in pathways:
    path_A = os.path.join(bed_dir, f"H3K4_A_{pathway}_genes_with_peaks.bed")
    path_N = os.path.join(bed_dir, f"H3K4_N_{pathway}_genes_with_peaks.bed")

    if os.path.exists(path_A) and os.path.exists(path_N):
        peaks_A = extract_peaks(path_A)
        peaks_N = extract_peaks(path_N)

        plt.figure(figsize=(5, 5))
        venn2([peaks_A, peaks_N], set_labels=(f"A", f"N"))
        plt.title(f"Peak Overlap in H3K4 (Pathway: {pathway.replace('_', ' ')})")

        out_file = f"venn_H3K4_{pathway}.png"
        plt.savefig(out_file, dpi=300)
        plt.show()
        print(f"Saved: {out_file}")
    else:
        print(f"Skipping {pathway}: one or both files missing.")