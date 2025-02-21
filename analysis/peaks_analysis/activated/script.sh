#!/bin/bash

cd ../../../analysis/activated/

# find multiinter
bedtools multiinter -i H3K4_A.macs2.consensus.peaks.awk.bed H3K4_N.macs2.consensus.peaks.awk.bed H3K27_A.macs2.consensus.peaks.awk.bed H3K27_N.macs2.consensus.peaks.awk.bed > multiinter_output.bed
