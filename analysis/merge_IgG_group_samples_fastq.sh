#!/bin/bash

cd ~/cut_run/fastq/

# IgG_A
zcat IgG_A_1_S21_L001_R2_001.fastq.gz IgG_A_2_S22_L001_R1_001.fastq.gz IgG_A_3_S23_L001_R2_001.fastq.gz IgG_A_4_S24_L001_R2_001.fastq.gz | gzip > IgG_A_merged_L001_R1.fastq.gz
zcat IgG_A_1_S21_L001_R2_001.fastq.gz IgG_A_2_S22_L001_R2_001.fastq.gz IgG_A_3_S23_L001_R2_001.fastq.gz IgG_A_4_S24_L001_R2_001.fastq.gz | gzip > IgG_A_merged_L001_R2.fastq.gz


# IgG_N
zcat IgG_N_1_S17_L001_R1_001.fastq.gz IgG_N_2_S18_L001_R1_001.fastq.gz IgG_N_3_S19_L001_R1_001.fastq.gz IgG_N_4_S20_L001_R1_001.fastq.gz | gzip > IgG_N_merged_L001_R1.fastq.gz
zcat IgG_N_1_S17_L001_R2_001.fastq.gz IgG_N_2_S18_L001_R2_001.fastq.gz IgG_N_3_S19_L001_R2_001.fastq.gz IgG_N_4_S20_L001_R2_001.fastq.gz | gzip > IgG_N_merged_L001_R2.fastq.gz


# nIgG_A
zcat nIgG_A_1_S37_L001_R1_001.fastq.gz nIgG_A_2_S38_L001_R1_001.fastq.gz | gzip > nIgG_A_merged_L001_R1.fastq.gz
zcat nIgG_A_1_S37_L001_R2_001.fastq.gz nIgG_A_2_S38_L001_R2_001.fastq.gz | gzip > nIgG_A_merged_L001_R2.fastq.gz


# nIgG_N
zcat nIgG_N_1_S39_L001_R1_001.fastq.gz nIgG_N_2_S40_L001_R1_001.fastq.gz | gzip > nIgG_N_merged_L001_R1.fastq.gz
zcat nIgG_N_1_S39_L001_R2_001.fastq.gz nIgG_N_2_S40_L001_R2_001.fastq.gz | gzip > nIgG_N_merged_L001_R2.fastq.gz