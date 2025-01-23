#!/bin/bash

cd ~/cut_run/results/03_peak_calling/05_consensus_peaks/macs2

# Define the groups to process
groups=("H3K4_A" "H3K4_N" "H3K27_A" "H3K27_N")

# Base directory for input files
base_dir="$HOME/cut_run/results/03_peak_calling/04_called_peaks/macs2"

# Loop over each group
for group in "${groups[@]}"; do
    # Define input files for the current group
    input_files=()
    for replicate in R1 R2 R3 R4; do
        file="$base_dir/${group}_${replicate}.macs2.peaks.cut.bed"
        if [[ -f "$file" ]]; then
            input_files+=("$file")
        fi
    done

    # Skip processing if fewer than 3 valid input files are found
    if [[ ${#input_files[@]} -lt 3 ]]; then
        echo "Error: Less than 3 valid input files found for group: $group. Skipping..."
        continue
    fi

    # Define output filenames
    merged_file="${group}.macs2.merged_peaks.bed"
    consensus_file="${group}.macs2.consensus.peak_counts.bed"
    filtered_file="${group}.macs2.consensus.peaks.awk3.bed"

    # Combine all input files into one, sort them, and merge overlapping peaks
    cat "${input_files[@]}" | \
    sort -k1,1 -k2,2n | \
    bedtools merge -c 4 -o distinct -delim "," -i - > "$merged_file"

    # Count the number of input files each peak is present in
    bedtools intersect -a "$merged_file" -b "${input_files[@]}" -c > "$consensus_file"

    # Filter peaks present in at least 3 files
    awk '$NF >= 3' "$consensus_file" > "$filtered_file"

    # Print a completion message for the current group
    echo "Processed group: $group"
    echo "  Merged file: $merged_file"
    echo "  Consensus file: $consensus_file"
    echo "  Filtered file (>=3 overlaps): $filtered_file"
done

# Print a final message
echo "All groups with 4 samples processed!"


# Define the groups to process
groups=("nH3K4_A" "nH3K4_N" "nH3K27_A" "nH3K27_N")

# Base directory for input files
base_dir="$HOME/cut_run/results/03_peak_calling/04_called_peaks/macs2"

# Loop over each group
for group in "${groups[@]}"; do
    # Define input files for the current group
    input_files=()
    for replicate in R1 R2 R3; do
        file="$base_dir/${group}_${replicate}.macs2.peaks.cut.bed"
        if [[ -f "$file" ]]; then
            input_files+=("$file")
        fi
    done

    # Skip processing if fewer than 2 valid input files are found
    if [[ ${#input_files[@]} -lt 2 ]]; then
        echo "Error: Less than 2 valid input files found for group: $group. Skipping..."
        continue
    fi

    # Define output filenames
    merged_file="${group}.macs2.merged_peaks.bed"
    consensus_file="${group}.macs2.consensus.peak_counts.bed"
    filtered_file="${group}.macs2.consensus.peaks.awk2.bed"

    # Combine all input files into one, sort them, and merge overlapping peaks
    cat "${input_files[@]}" | \
    sort -k1,1 -k2,2n | \
    bedtools merge -c 4 -o distinct -delim "," -i - > "$merged_file"

    # Count the number of input files each peak is present in
    bedtools intersect -a "$merged_file" -b "${input_files[@]}" -c > "$consensus_file"

    # Filter peaks present in at least 2 files
    awk '$NF >= 2' "$consensus_file" > "$filtered_file"

    # Print a completion message for the current group
    echo "Processed group: $group"
    echo "  Merged file: $merged_file"
    echo "  Consensus file: $consensus_file"
    echo "  Filtered file (>=2 overlaps): $filtered_file"
done

# Print a final message
echo "All groups with 3 samples processed!"