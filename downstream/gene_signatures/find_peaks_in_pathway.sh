#!/bin/bash

# Ensure bedtools is installed
which bedtools > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Error: bedtools is not installed or not in your PATH."
    exit 1
fi

# Create output directories if needed
mkdir -p H3K4 H3K27

# Define pathways
pathways=(
  tgf_beta_signaling
  il2_stat5_signaling
  il6_jak_stat3_signaling
  effector_vs_memory_cd8_up
  effector_vs_memory_cd8_dn
  tcr
  housekeeping
  methionine
)

# Intersect for H3K4
for pathway in "${pathways[@]}"; do
  peak_A="H3K4/H3K4_A.macs2.consensus.peaks.awk.bed"
  peak_N="H3K4/H3K4_N.macs2.consensus.peaks.awk.bed"
  genes="genelocs_${pathway}.bed"

  out_A="H3K4/H3K4_A_${pathway}_peaks_gene_intersections.bed"
  out_N="H3K4/H3K4_N_${pathway}_peaks_gene_intersections.bed"

  bedtools intersect -a "$peak_A" -b "$genes" -u > "$out_A"
  echo "Intersection saved to $out_A"

  bedtools intersect -a "$peak_N" -b "$genes" -u > "$out_N"
  echo "Intersection saved to $out_N"
done

# Intersect for H3K27
for pathway in "${pathways[@]}"; do
  peak_A="H3K27/H3K27_A.macs2.consensus.peaks.awk.bed"
  peak_N="H3K27/H3K27_N.macs2.consensus.peaks.awk.bed"
  genes="genelocs_${pathway}.bed"

  out_A="H3K27/H3K27_A_${pathway}_peaks_gene_intersections.bed"
  out_N="H3K27/H3K27_N_${pathway}_peaks_gene_intersections.bed"

  bedtools intersect -a "$peak_A" -b "$genes" -u > "$out_A"
  echo "Intersection saved to $out_A"

  bedtools intersect -a "$peak_N" -b "$genes" -u > "$out_N"
  echo "Intersection saved to $out_N"
done