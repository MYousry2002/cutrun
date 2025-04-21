# extract_hallmark_gene_locs.py
import pandas as pd
import json
import gffutils
import os

gtf = "Mus_musculus.GRCm38.102.gtf"
json_sets = "go_bp_mouse.json"
out_dir = "go_bp_beds"
os.makedirs(out_dir, exist_ok=True)

# Create/load DB
db_file = gtf + ".db"
try:
    db = gffutils.FeatureDB(db_file)
except:
    db = gffutils.create_db(gtf, dbfn=db_file, force=True, keep_order=True,
                            disable_infer_transcripts=True, disable_infer_genes=True)

with open(json_sets) as f:
    gene_sets = json.load(f)["sets"]

for set_name, genes in gene_sets.items():
    records = []
    for gene in db.features_of_type("gene"):
        gname = gene.attributes.get("gene_name", [None])[0]
        if gname in genes:
            chrom = gene.chrom if gene.chrom.startswith("chr") else f"chr{gene.chrom}"
            records.append([chrom, gene.start, gene.end, gname])
    if records:
        df = pd.DataFrame(records, columns=["Chrom", "Start", "End", "Gene"])
        df.to_csv(f"{out_dir}/{set_name}.bed", sep="\t", index=False, header=False)