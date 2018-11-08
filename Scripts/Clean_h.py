import pandas as pd

def clean_h(input_file, output_file):
    in_file = pd.read_table(input_file, sep='\t', skiprows=1, header=None)
    in_file.dropna(inplace=True)
    cols = in_file.shape[1]
    for i in range(cols):
        in_file.drop_duplicates(subset=[i], keep=False, inplace=True)
    in_file.to_csv(output_file, sep='\t', index=False, header=None)
    return print('Done Clean_h')

clean_h(r'C:\Users\1\Desktop\Data\gam_atr\import\0_homology_genes.tsv', r'C:\Users\1\Desktop\Data\gam_atr\clean\0_homology_genes.tsv')