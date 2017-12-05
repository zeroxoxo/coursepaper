import pandas as pd
def clean_g(path):
    ref = pd.read_table(path + '0_homology_genes.tsv', sep='\t')
    rows, col = ref.shape()
    for i in range(col):
        j = pd.read_table(path + str(i) + '_gene.tsv', header=False, sep='\t')
        g = j.loc[j[j.columns[4]].isin(ref[ref.columns[i]])]]
        g.to_csv(path + str(i) + '_clean_genes.tsv', sep='\t')