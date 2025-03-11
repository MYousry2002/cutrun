import json
import pandas as pd
import gffutils

def extract_gene_locations(gtf_file, json_file, output_file):
    """
    Extracts gene locations from a GTF annotation file based on a list of mouse genes in JSON format.

    Parameters:
    gtf_file (str): Path to the GTF file.
    json_file (str): Path to the JSON file containing the list of genes.
    output_file (str): Path to save the extracted gene locations.
    """
    
    # Load gene list from JSON
    with open(json_file, 'r') as f:
        gene_data = json.load(f)
    gene_list = set(gene_data.get("genes", []))

    # Create or load GTF database
    db_file = gtf_file + ".db"
    try:
        db = gffutils.FeatureDB(db_file)
    except:
        db = gffutils.create_db(gtf_file, dbfn=db_file, force=True, keep_order=True, disable_infer_transcripts=True, disable_infer_genes=True)

    # Extract gene locations
    gene_locations = []
    for gene in db.features_of_type("gene"):
        gene_name = gene.attributes.get("gene_name", [None])[0]  # Adjust key based on GTF source
        if gene_name in gene_list:
            gene_locations.append([gene_name, gene.chrom, gene.start, gene.end, gene.strand])

    # Save results
    df = pd.DataFrame(gene_locations, columns=["Gene", "Chromosome", "Start", "End", "Strand"])
    
    # Ensure chromosome names start with "chr"
    df["Chromosome"] = df["Chromosome"].astype(str)
    df["Chromosome"] = df["Chromosome"].apply(lambda x: f"chr{x}" if not x.startswith("chr") else x)

    df.to_csv(output_file, sep="\t", index=False)
    
    print(f"Extracted {len(df)} gene locations. Saved to {output_file}")


def convert_gene_locs_to_bed(gene_loc_file, output_bed):
    """
    Convert gene locations from TSV to BED format and ensure proper chromosome naming.
    
    Parameters:
    gene_loc_file (str): Input gene locations file (TSV format).
    output_bed (str): Output BED file.
    """
    df = pd.read_csv(gene_loc_file, sep="\t")

    # Ensure the required columns exist
    required_columns = ["Chromosome", "Start", "End", "Gene"]
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"Missing required columns in {gene_loc_file}")

    # Ensure chromosome names start with "chr"
    df["Chromosome"] = df["Chromosome"].astype(str)
    df["Chromosome"] = df["Chromosome"].apply(lambda x: f"chr{x}" if not x.startswith("chr") else x)

    # BED format: Chromosome, Start, End, Gene Name
    df_bed = df[["Chromosome", "Start", "End", "Gene"]]
    df_bed.to_csv(output_bed, sep="\t", header=False, index=False)

    print(f"Converted {gene_loc_file} to BED format: {output_bed}")


# Define GTF file
gtf_file = "Mus_musculus.GRCm38.102.gtf"

"""

# IL-2/STAT5 signaling
json_file = "il2_stat5_signaling.json"
output_file = "genelocs_il2_stat5_signaling.tsv"
extract_gene_locations(gtf_file, json_file, output_file)
output_bed = "genelocs_il2_stat5_signaling.bed"
convert_gene_locs_to_bed(output_file, output_bed)

# IL-6/JAK/STAT3 signaling
json_file = "il6_jak_stat3_signaling.json"
output_file = "genelocs_il6_jak_stat3_signaling.tsv"
extract_gene_locations(gtf_file, json_file, output_file)
output_bed = "genelocs_il6_jak_stat3_signaling.bed"
convert_gene_locs_to_bed(output_file, output_bed)

# TGF-beta signaling
json_file = "tgf_beta_signaling.json"
output_file = "genelocs_tgf_beta_signaling.tsv"
extract_gene_locations(gtf_file, json_file, output_file)
output_bed = "genelocs_tgf_beta_signaling.bed"
convert_gene_locs_to_bed(output_file, output_bed)

# effector_vs_memory_cd8_up
json_file = "effector_vs_memory_cd8_up.json"
output_file = "genelocs_effector_vs_memory_cd8_up.tsv"
extract_gene_locations(gtf_file, json_file, output_file)
output_bed = "genelocs_effector_vs_memory_cd8_up.bed"
convert_gene_locs_to_bed(output_file, output_bed)

# effector_vs_memory_cd8_dn
json_file = "effector_vs_memory_cd8_dn.json"
output_file = "genelocs_effector_vs_memory_cd8_dn.tsv"
extract_gene_locations(gtf_file, json_file, output_file)
output_bed = "genelocs_effector_vs_memory_cd8_dn.bed"
convert_gene_locs_to_bed(output_file, output_bed)

# TCR pathway
json_file = "tcr.json"
output_file = "genelocs_tcr.tsv"
extract_gene_locations(gtf_file, json_file, output_file)
output_bed = "genelocs_tcr.bed"
convert_gene_locs_to_bed(output_file, output_bed)

"""
# housekeeping genes
json_file = "housekeeping.json"
output_file = "housekeeping.tsv"
extract_gene_locations(gtf_file, json_file, output_file)
output_bed = "genelocs_housekeeping.bed"
convert_gene_locs_to_bed(output_file, output_bed)