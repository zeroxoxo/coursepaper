import click
import pandas as pd
import os
from biomart import BiomartServer
server = BiomartServer('http://biomart.vectorbase.org/biomart/')
def search(path, ds):
    for i in ds:
        r = server.datasets[i + '_eg_gene'].search({
            'filters': {},
            'attributes': [ 'chromosome_name', 'start_position', 'end_position', 'strand', 'ensembl_gene_id' ]
        })
        name = path + str(ds.index(i)) + '_gene.tsv'
        f = open(name, 'w')
        f.close()
        f = open(name, 'a')
        for line in r.iter_lines():
            line = line.decode('utf-8')
            f.write(line + '\n')
        f.close()

    l = ['ensembl_gene_id']
    for k in range(len(ds)-1):
        l.append(ds[k+1]+'_eg_homolog_ensembl_gene')
    s = server.datasets[ds[0]+'_eg_gene'].search({
        'filters': {},
        'attributes': l
    }, header = 1)
    name1 = path + '0_homology_genes.tsv'
    f = open(name1, 'w')
    f.close()
    f = open(name1, 'a')
    for line in s.iter_lines():
        line = line.decode('utf-8')
        f.write(line + '\n')
    f.close()
    return print('VB done.')

def clean_h(input_file, output_file):
    in_file = pd.read_table(input_file, sep='\t').dropna()
    rows, cols = in_file.shape
    for i in range(cols):
        in_file = in_file.drop_duplicates(subset=in_file.iloc[:,[i]], keep=False)
    in_file.to_csv(output_file, sep='\t', index=False)
    return print('Done Clean_h.')

def clean_g(h_path, g_path):
    ref = pd.read_table(h_path + '0_homology_genes.tsv', sep='\t')
    rows, col = ref.shape
    for i in range(col):
        j = pd.read_table(g_path + str(i) + '_gene.tsv', header=None, sep='\t')
        g = j.loc[j[j.columns[4]].isin(ref[ref.columns[i]])]
        g.to_csv(h_path + str(i) + '_clean_genes.tsv', sep='\t', header=False, index=False)
    return print('Done Clean_g')

@click.command()
@click.argument('ds', nargs=-1)
@click.argument('path', nargs=1, type=click.Path(exists=True))
def Workflow(ds, path):
    os.makedirs(path + '/clean/')
    os.makedirs(path + '/import/')
    search(path + '/import/', ds)
    clean_h(path + '/import/0_homology_genes.tsv', path + '/clean/0_homology_genes.tsv')
    clean_g(path + '/clean/', path + '/import/')
    click.echo('Done')