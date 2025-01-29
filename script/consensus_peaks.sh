# refilter naive consensus to include peaks common in 2 samples instead of 3

cd ../results/03_peak_calling/05_consensus_peaks

awk '$NF >= 2' nH3K4_A.macs2.consensus.peak_counts.bed > nH3K4_A.macs2.consensus.peaks.awk2.bed

awk '$NF >= 2' nH3K4_N.macs2.consensus.peak_counts.bed > nH3K4_N.macs2.consensus.peaks.awk2.bed

awk '$NF >= 2' nH3K27_A.macs2.consensus.peak_counts.bed > nH3K27_A.macs2.consensus.peaks.awk2.bed

awk '$NF >= 2' nH3K27_N.macs2.consensus.peak_counts.bed > nH3K27_N.macs2.consensus.peaks.awk2.bed