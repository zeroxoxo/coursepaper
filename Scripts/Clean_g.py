import pandas as pd

def clean_g(h_path, g_path):
    ref = pd.read_table(h_path + '0_homology_genes.tsv', sep='\t', header=None)
    rows, col = ref.shape
    for i in range(col):
        j = pd.read_table(g_path + str(i) + '_gene.tsv', sep='\t', header=None)
        g = j.loc[j[4].isin(ref[i])]
        #g = j.loc[j[j.columns[4]].isin(ref[ref.columns[i]])]
        g.to_csv(h_path + str(i) + '_clean_genes.tsv', sep='\t', header=False, index=False)
    return print('Done Clean_g')

clean_g(r'C:\Users\1\Desktop\Data\gam_atr\clean/', r'C:\Users\1\Desktop\Data\gam_atr\import/')