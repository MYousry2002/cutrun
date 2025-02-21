#!/bin/bash

# common peaks in all files
cd ../../../analysis/activated/
awk '$4 == 4' multiinter_output.bed > common_peaks_all.bed

# Extract peaks that are found in **only** the first and second samples
awk '$4 == 2 && $5 == "1,2"' multiinter_output.bed > common_peaks_H3K4_AN.bed
echo "Filtered peaks saved to common_peaks_H3K4_AN.bed"


# Extract peaks that are found in **only** the third and fourth samples
awk '$4 == 2 && $5 == "3,4"' multiinter_output.bed > common_peaks_H3K27_AN.bed
echo "Filtered peaks saved to common_peaks_H3K27_AN.bed"


# Extract peaks that are found in **only** the first and third samples
awk '$4 == 2 && $5 == "1,3"' multiinter_output.bed > common_peaks_H3K4A_H3K27A.bed
echo "Filtered peaks saved to common_peaks_H3K4A_H3K27A.bed"


# Extract peaks that are found in **only** the second and fourth samples
awk '$4 == 2 && $5 == "2,4"' multiinter_output.bed > common_peaks_H3K4N_H3K27N.bed
echo "Filtered peaks saved to common_peaks_H3K4N_H3K27N.bed"