import pandas as pd
def clean_g(h_path, g_path):
    ref = pd.read_table(h_path + '0_homology_genes.tsv', sep='\t')
    rows, col = ref.shape
    for i in range(col):
        j = pd.read_table(g_path + str(i) + '_gene.tsv', header=None, sep='\t')
        g = j.loc[j[j.columns[4]].isin(ref[ref.columns[i]])]
        g.to_csv(h_path + str(i) + '_clean_genes.tsv', sep='\t', header=False, index=False)
    return print('Done')

clean_g('~/coursepaper/Data/temp/clean/', '~/coursepaper/Data/temp/imp/')