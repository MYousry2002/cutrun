#!/bin/bash
#$ -cwd
#$ -N run_pipeline
#$ -o run_pipeline.out
#$ -e run_pipeline.err
#$ -l h_vmem=1024G
#$ -pe smp 16
#$ -l h_rt=24:00:00


# Set the working directory
cd ~/cutrun

# Activate conda environment
source /home/me1117/anaconda3/etc/profile.d/conda.sh
conda activate /home/me1117/anaconda3/envs/nextflow_env

# Run the pipeline
nextflow run nf-core/cutandrun -profile docker --input ./samplesheet.csv --genome mm10 --outdir ./results  --replicate_threshold 3  --normalisation_mode CPM --peakcaller MACS2 -resume
