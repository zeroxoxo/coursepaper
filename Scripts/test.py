import pandas as pd
def test_homology_file_duplicate(file):
    homology = pd.read_table(file, header=None, sep='\t')
    rows, cols = homology.shape
    for i in range(cols):
        f = homology.iloc[:, i].duplicated(keep=False)
        for j in f:
            if j == True:
                return print('Oops')
    return print("It's okay, man")

test_homology_file_duplicate('~/coursepaper/output/temp/clean/0_homology_genes.tsv')