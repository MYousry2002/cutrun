#!/bin/bash

cd ../../../analysis/naive

# find multiinter
bedtools multiinter -i nH3K4_A.macs2.consensus.peaks.awk2.bed nH3K4_N.macs2.consensus.peaks.awk2.bed nH3K27_A.macs2.consensus.peaks.awk2.bed nH3K27_N.macs2.consensus.peaks.awk2.bed > multiinter_output.bed
