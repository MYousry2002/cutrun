# hallmark_combined_peak_enrichment.py
import os
import glob
import pandas as pd
import numpy as np
from scipy.stats import fisher_exact
from statsmodels.stats.multitest import multipletests

# Directories
gene_bed_dir = "hallmark_beds/"
output_dir = "intersections"
os.makedirs(output_dir, exist_ok=True)

# Peak files
peak_files = {
    "H3K4_A": "H3K4/H3K4_A.macs2.consensus.peaks.awk.bed",
    "H3K4_N": "H3K4/H3K4_N.macs2.consensus.peaks.awk.bed",
    "H3K27_A": "H3K27/H3K27_A.macs2.consensus.peaks.awk.bed",
    "H3K27_N": "H3K27/H3K27_N.macs2.consensus.peaks.awk.bed",
}

# Count total peaks
total_peaks = {}
for label, file_path in peak_files.items():
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Missing peak file: {file_path}")
    total_peaks[label] = sum(1 for _ in open(file_path))

# Process each gene set and histone mark
results = []

for mark in ["H3K4", "H3K27"]:
    for gene_bed in glob.glob(os.path.join(gene_bed_dir, "*.bed")):
        pathway = os.path.basename(gene_bed).replace(".bed", "")
        counts = {}

        for cond in ["A", "N"]:
            label = f"{mark}_{cond}"
            intersect_file = os.path.join(output_dir, f"{label}_{pathway}.bed")
            cmd = f"bedtools intersect -a {peak_files[label]} -b {gene_bed} -u > {intersect_file}"
            os.system(cmd)

            if not os.path.exists(intersect_file):
                raise RuntimeError(f"Failed to generate intersection: {intersect_file}")

            counts[label] = sum(1 for _ in open(intersect_file))

        # Calculate stats
        A = counts[f"{mark}_A"]
        N = counts[f"{mark}_N"]
        total_A = total_peaks[f"{mark}_A"]
        total_N = total_peaks[f"{mark}_N"]

        prop_A = A / total_A if total_A > 0 else 0
        prop_N = N / total_N if total_N > 0 else 0
        log2_fc = np.log2(prop_A / prop_N) if prop_A > 0 and prop_N > 0 else np.nan

        # Fisher’s exact test
        contingency = [[A, total_A - A], [N, total_N - N]]
        odds_ratio, p_value = fisher_exact(contingency)

        results.append({
            "Pathway": pathway,
            "Mark": mark,
            "Adult_Peaks": A,
            "Neonate_Peaks": N,
            "Total_Adult_Peaks": total_A,
            "Total_Neonate_Peaks": total_N,
            "Prop_Adult": prop_A,
            "Prop_Neonate": prop_N,
            "Log2_FC": log2_fc,
            "Odds_Ratio": odds_ratio,
            "P_Value": p_value,
            "Direction": "Adult > Neonate" if prop_A > prop_N else "Neonate > Adult" if prop_N > prop_A else "Equal"
        })

# Compile results and adjust for multiple testing
df = pd.DataFrame(results)
df["FDR"] = multipletests(df["P_Value"], method="fdr_bh")[1]
df = df.sort_values("FDR")

# Save results
df.to_csv("hallmark_peak_enrichment_combined.tsv", sep="\t", index=False)
print("Saved results to hallmark_peak_enrichment_combined.tsv")