import pandas as pd

def k_way(path):
    ref = pd.read_table(path + '0_homology_genes.tsv', header=None, sep='\t')
    rows, col = ref.shape
    out = pd.Series([out for out in range(rows)], name='id')
    for i in range(col):
        j = pd.read_table(path + str(i) + '_clean_genes.tsv', header=None, sep='\t')
        p = pd.merge(ref, j, how='inner', left_on=ref.iloc[:,i], right_on=j.iloc[:, 4], validate='one_to_one')
        p[2] = p[2] - p['1_y']
        p.rename({'0_y': 'genome'+str(i+1)+'_chr', '1_y': 'genome'+str(i+1)+'_start', 2: 'genome'+str(i+1)+'_len',
                          3 : 'genome'+str(i+1)+'_sign'}, axis='columns', inplace=True)
        out = pd.concat([out, p.iloc[:,3:7]], join='inner', axis=1)
    out.to_csv(path + 'k_way_anchors.tsv', sep='\t', index=False)
    return

k_way(r'C:\Users\1\Desktop\Data\gam_atr\clean\\')