import pandas as pd
path = 'c:/users/1/pycharmprojects/coursepaper/output/clean/'
def k_way(h_path):
    ref = pd.read_table(h_path + '0_homology_genes.tsv',header=None, sep='\t')
    rows, col = ref.shape
    out = pd.Series([out for out in range(rows)],name='id')
    for i in range(col):
        j = pd.read_table(h_path + str(i) + '_clean_genes.tsv', header=None, sep='\t')
        p = pd.merge(ref, j, how='inner', left_on=ref.iloc[:,i], right_on=j.iloc[:, 4],)
        p['2_y'] = p['2_y'] - p['1_y']
        p.rename_axis({'0_y': 'genome'+str(i+1)+'_chr', '1_y': 'genome'+str(i+1)+'_start', '2_y': 'genome'+str(i+1)+'_len',
                          3 : 'genome'+str(i+1)+'_sign'}, axis='columns', inplace=True)
        out = pd.concat([out, p.iloc[:,3:7]], join='inner', axis=1)
    print(out.head())
    return
k_way(path)