#!/bin/bash

# Ensure bedtools is installed and in your path
which bedtools > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Error: bedtools is not installed or not in your PATH."
    exit 1
fi

# Fix chromosome naming if necessary
awk '{if ($1 !~ /^chr/) print "chr"$0; else print $0}' genelocs_tgf_beta_signaling.bed > genelocs_tgf_beta_signaling_fixed.bed


# Run bedtools intersect to find any overlap

### H3K4

# tgf_beta
bedtools intersect -a genelocs_tgf_beta_signaling.bed -b H3K4/H3K4_A.macs2.consensus.peaks.awk.bed    -wa -wb > H3K4/H3K4_A_tgfb_peaks_gene_intersections.bed
echo "Intersection saved to H3K4_A_tgfb_peaks_gene_intersections.bed"

bedtools intersect -a genelocs_tgf_beta_signaling.bed -b H3K4/H3K4_N.macs2.consensus.peaks.awk.bed    -wa -wb > H3K4/H3K4_N_tgfb_peaks_gene_intersections.bed
echo "Intersection saved to H3K4_N_tgfb_peaks_gene_intersections.bed"

# il2
bedtools intersect -a genelocs_il2_stat5_signaling.bed -b H3K4/H3K4_A.macs2.consensus.peaks.awk.bed    -wa -wb > H3K4/H3K4_A_il2_peaks_gene_intersections.bed
echo "Intersection saved to H3K4_A_il2_peaks_gene_intersections.bed"

bedtools intersect -a genelocs_il2_stat5_signaling.bed -b H3K4/H3K4_N.macs2.consensus.peaks.awk.bed    -wa -wb > H3K4/H3K4_N_il2_peaks_gene_intersections.bed
echo "Intersection saved to H3K4_N_il2_peaks_gene_intersections.bed"

# il6
bedtools intersect -a genelocs_il6_jak_stat3_signaling.bed -b H3K4/H3K4_A.macs2.consensus.peaks.awk.bed    -wa -wb > H3K4/H3K4_A_il6_peaks_gene_intersections.bed
echo "Intersection saved to H3K4_A_il2_peaks_gene_intersections.bed"

bedtools intersect -a genelocs_il6_jak_stat3_signaling.bed -b H3K4/H3K4_N.macs2.consensus.peaks.awk.bed    -wa -wb > H3K4/H3K4_N_il6_peaks_gene_intersections.bed
echo "Intersection saved to H3K4_N_il6_peaks_gene_intersections.bed"


# Effector vs memory cd8 up
bedtools intersect -a genelocs_effector_vs_memory_cd8_up.bed -b H3K4/H3K4_A.macs2.consensus.peaks.awk.bed    -wa -wb > H3K4/H3K4_A_eff_peaks_gene_intersections.bed
echo "Intersection saved to H3K4_A_eff_peaks_gene_intersections.bed"

bedtools intersect -a genelocs_effector_vs_memory_cd8_up.bed -b H3K4/H3K4_N.macs2.consensus.peaks.awk.bed    -wa -wb > H3K4/H3K4_N_eff_peaks_gene_intersections.bed
echo "Intersection saved to H3K4_N_eff_peaks_gene_intersections.bed"

# Effector vs memory cd8 dn
bedtools intersect -a genelocs_effector_vs_memory_cd8_dn.bed -b H3K4/H3K4_A.macs2.consensus.peaks.awk.bed    -wa -wb > H3K4/H3K4_A_mem_peaks_gene_intersections.bed
echo "Intersection saved to H3K4_A_mem_peaks_gene_intersections.bed"

bedtools intersect -a genelocs_effector_vs_memory_cd8_dn.bed -b H3K4/H3K4_N.macs2.consensus.peaks.awk.bed    -wa -wb > H3K4/H3K4_N_mem_peaks_gene_intersections.bed
echo "Intersection saved to H3K4_N_mem_peaks_gene_intersections.bed"

#  tcr
bedtools intersect -a genelocs_tcr.bed -b H3K4/H3K4_A.macs2.consensus.peaks.awk.bed    -wa -wb > H3K4/H3K4_A_tcr_peaks_gene_intersections.bed
echo "Intersection saved to H3K4_A_tcr_peaks_gene_intersections.bed"

bedtools intersect -a genelocs_tcr.bed -b H3K4/H3K4_N.macs2.consensus.peaks.awk.bed    -wa -wb > H3K4/H3K4_N_tcr_peaks_gene_intersections.bed
echo "Intersection saved to H3K4_N_tcr_peaks_gene_intersections.bed"


# housekeeping
bedtools intersect -a genelocs_housekeeping.bed -b H3K4/H3K4_A.macs2.consensus.peaks.awk.bed    -wa -wb > H3K4/H3K4_A_housekeeping_peaks_gene_intersections.bed
echo "Intersection saved to H3K4_A_housekeeping_peaks_gene_intersections.bed"

bedtools intersect -a genelocs_housekeeping.bed -b H3K4/H3K4_N.macs2.consensus.peaks.awk.bed    -wa -wb > H3K4/H3K4_N_housekeeping_peaks_gene_intersections.bed
echo "Intersection saved to H3K4_N_housekeeping_peaks_gene_intersections.bed"

# methionine
bedtools intersect -a genelocs_methionine.bed -b H3K4/H3K4_A.macs2.consensus.peaks.awk.bed    -wa -wb > H3K4/H3K4_A_methionine_peaks_gene_intersections.bed
echo "Intersection saved to H3K4_A_methionine_peaks_gene_intersections.bed"

bedtools intersect -a genelocs_methionine.bed -b H3K4/H3K4_N.macs2.consensus.peaks.awk.bed    -wa -wb > H3K4/H3K4_N_methionine_peaks_gene_intersections.bed
echo "Intersection saved to H3K4_N_methionine_peaks_gene_intersections.bed"


### H3K27

# tgf_beta
bedtools intersect -a genelocs_tgf_beta_signaling.bed -b H3K27/H3K27_A.macs2.consensus.peaks.awk.bed    -wa -wb > H3K27/H3K27_A_tgfb_peaks_gene_intersections.bed
echo "Intersection saved to H3K27_A_tgfb_peaks_gene_intersections.bed"

bedtools intersect -a genelocs_tgf_beta_signaling.bed -b H3K27/H3K27_N.macs2.consensus.peaks.awk.bed    -wa -wb > H3K27/H3K27_N_tgfb_peaks_gene_intersections.bed
echo "Intersection saved to H3K27_N_tgfb_peaks_gene_intersections.bed"

# il2
bedtools intersect -a genelocs_il2_stat5_signaling.bed -b H3K27/H3K27_A.macs2.consensus.peaks.awk.bed    -wa -wb > H3K27/H3K27_A_il2_peaks_gene_intersections.bed
echo "Intersection saved to H3K27_A_il2_peaks_gene_intersections.bed"

bedtools intersect -a genelocs_il2_stat5_signaling.bed -b H3K27/H3K27_N.macs2.consensus.peaks.awk.bed    -wa -wb > H3K27/H3K27_N_il2_peaks_gene_intersections.bed
echo "Intersection saved to H3K27_N_il2_peaks_gene_intersections.bed"

# il6
bedtools intersect -a genelocs_il6_jak_stat3_signaling.bed -b H3K27/H3K27_A.macs2.consensus.peaks.awk.bed    -wa -wb > H3K27/H3K27_A_il6_peaks_gene_intersections.bed
echo "Intersection saved to H3K27_A_il6_peaks_gene_intersections.bed"

bedtools intersect -a genelocs_il6_jak_stat3_signaling.bed -b H3K27/H3K27_N.macs2.consensus.peaks.awk.bed    -wa -wb > H3K27/H3K27_N_il6_peaks_gene_intersections.bed
echo "Intersection saved to H3K27_N_il6_peaks_gene_intersections.bed"

# Effector vs memory cd8 up
bedtools intersect -a genelocs_effector_vs_memory_cd8_up.bed -b H3K27/H3K27_A.macs2.consensus.peaks.awk.bed    -wa -wb > H3K27/H3K27_A_eff_peaks_gene_intersections.bed
echo "Intersection saved to H3K27_A_eff_peaks_gene_intersections.bed"

bedtools intersect -a genelocs_effector_vs_memory_cd8_up.bed -b H3K27/H3K27_N.macs2.consensus.peaks.awk.bed    -wa -wb > H3K27/H3K27_N_eff_peaks_gene_intersections.bed
echo "Intersection saved to H3K27_N_eff_peaks_gene_intersections.bed"

# Effector vs memory cd8 dn
bedtools intersect -a genelocs_effector_vs_memory_cd8_dn.bed -b H3K27/H3K27_A.macs2.consensus.peaks.awk.bed    -wa -wb > H3K27/H3K27_A_mem_peaks_gene_intersections.bed
echo "Intersection saved to H3K27_A_mem_peaks_gene_intersections.bed"

bedtools intersect -a genelocs_effector_vs_memory_cd8_dn.bed -b H3K27/H3K27_N.macs2.consensus.peaks.awk.bed    -wa -wb > H3K27/H3K27_N_mem_peaks_gene_intersections.bed
echo "Intersection saved to H3K27_N_mem_peaks_gene_intersections.bed"

# tcr
bedtools intersect -a genelocs_tcr.bed -b H3K27/H3K27_A.macs2.consensus.peaks.awk.bed    -wa -wb > H3K27/H3K27_A_tcr_peaks_gene_intersections.bed
echo "Intersection saved to H3K27_A_tcr_peaks_gene_intersections.bed"

bedtools intersect -a genelocs_tcr.bed -b H3K27/H3K27_N.macs2.consensus.peaks.awk.bed    -wa -wb > H3K27/H3K27_N_tcr_peaks_gene_intersections.bed
echo "Intersection saved to H3K27_N_tcr_peaks_gene_intersections.bed"


# housekeeping
bedtools intersect -a genelocs_housekeeping.bed -b H3K27/H3K27_A.macs2.consensus.peaks.awk.bed    -wa -wb > H3K27/H3K27_A_housekeeping_peaks_gene_intersections.bed
echo "Intersection saved to H3K27_A_housekeeping_peaks_gene_intersections.bed"

bedtools intersect -a genelocs_housekeeping.bed -b H3K27/H3K27_N.macs2.consensus.peaks.awk.bed    -wa -wb > H3K27/H3K27_N_housekeeping_peaks_gene_intersections.bed
echo "Intersection saved to H3K27_N_housekeeping_peaks_gene_intersections.bed"


# methionine
bedtools intersect -a genelocs_methionine.bed -b H3K27/H3K27_A.macs2.consensus.peaks.awk.bed    -wa -wb > H3K27/H3K27_A_methionine_peaks_gene_intersections.bed
echo "Intersection saved to H3K27_A_methionine_peaks_gene_intersections.bed"

bedtools intersect -a genelocs_methionine.bed -b H3K27/H3K27_N.macs2.consensus.peaks.awk.bed    -wa -wb > H3K27/H3K27_N_methionine_peaks_gene_intersections.bed
echo "Intersection saved to H3K27_N_methionine_peaks_gene_intersections.bed"