# convert_gmt_to_json.py
import json

def gmt_to_dict(gmt_path):
    gene_sets = {}
    with open(gmt_path, 'r') as f:
        for line in f:
            parts = line.strip().split("\t")
            name = parts[0]
            genes = list(set(parts[2:]))
            gene_sets[name] = genes
    return gene_sets

gmt_file = "m5.all.v2024.1.Mm.symbols.gmt"
out_json = "go_bp_mouse.json"
gene_sets = gmt_to_dict(gmt_file)

with open(out_json, "w") as f:
    json.dump({"sets": gene_sets}, f, indent=2)

print(f"Saved {len(gene_sets)} Hallmark sets to {out_json}")