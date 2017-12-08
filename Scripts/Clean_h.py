import pandas as pd
def clean(input_file, output_file):
    in_file = pd.read_table(input_file, sep='\t').dropna()
    rows, cols = in_file.shape
    for i in range(cols):
        in_file = in_file.drop_duplicates(subset=in_file.iloc[:,[i]], keep=False)
    in_file.to_csv(output_file, sep='\t', index=False)
    return print('Done')

clean('/home/lab51/coursepaper/Data/temp/imp/0_homology_genes.tsv', '/home/lab51/coursepaper/Data/temp/clean/0_homology_genes.tsv')