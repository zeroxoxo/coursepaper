import pandas as pd
import numpy as np
def test_homology_file(file):
    homology = pd.read_table(file, header=None, sep='\t')
    rows, cols = homology.shape
    for i in range(cols):
        f = homology.iloc[:, i]
        g = f.duplicated(keep=False)
        for j in g:
            if j:
                return print('Oops')
        for k in f:
            if k == np.nan:
                return print('Oops')

    return print("It's okay, man")

test_homology_file('/home/lab51/coursepaper/output/temp/clean/0_homology_genes.tsv')

