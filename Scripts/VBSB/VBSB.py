import time
start_time = time.time()
import click
import pandas as pd
import os
from biomart import BiomartServer
import subprocess as sp

server = BiomartServer('http://biomart.vectorbase.org/biomart/')

def search(path, ds):
    for i in ds:
        name = path + str(ds.index(i)) + '_gene.tsv'
        f = open(name, 'w')
        f.close()
        f = open(name, 'a')
        r = server.datasets[i + '_eg_gene'].search({
            'filters': {},
            'attributes': ['chromosome_name', 'start_position', 'end_position', 'strand', 'ensembl_gene_id']
        })
        for line in r.iter_lines():
            line = line.decode('utf-8')
            f.write(line + '\n')
    f.close()

    l = ['ensembl_gene_id']
    name1 = path + '0_homology_genes.tsv'
    f = open(name1, 'w')
    f.close()
    f = open(name1, 'a')
    for k in range(len(ds)-1):
        l.append(ds[k+1]+'_eg_homolog_ensembl_gene')
    for v in ['2L', '2R', '3L', '3R', 'X']:
        s = server.datasets[ds[0]+'_eg_gene'].search({
            'filters': {'chromosome_name': v},
            'attributes': l
        }, header = 1)

        for line in s.iter_lines():
            line = line.decode('utf-8')
            f.write(line + '\n')
    f.close()
    return print('VB done.')

def clean_h(input_file, output_file):
    in_file = pd.read_table(input_file, sep='\t', skiprows=1, header=None)
    in_file.dropna(inplace=True)
    cols = in_file.shape[1]
    for i in range(cols):
        in_file.drop_duplicates(subset=[i], keep=False, inplace=True)
    in_file.to_csv(output_file, sep='\t', index=False, header=None)
    return print('Done Clean_h')

def clean_g(h_path, g_path):
    ref = pd.read_table(h_path + '0_homology_genes.tsv', sep='\t', header=None)
    rows, col = ref.shape
    for i in range(col):
        j = pd.read_table(g_path + str(i) + '_gene.tsv', sep='\t', header=None)
        g = j.loc[j[4].isin(ref[i])]
        #g = j.loc[j[j.columns[4]].isin(ref[ref.columns[i]])]
        g.to_csv(h_path + str(i) + '_clean_genes.tsv', sep='\t', header=False, index=False)
    return print('Done Clean_g')

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

@click.command()
@click.argument('ds', nargs=-1)
@click.argument('path', nargs=1, type=click.Path(exists=True))
def Workflow(ds, path):
    f = path + '/clean/k_way_anchors.tsv'
    d = path + '/clean/grimm_a_output'
    os.makedirs(path + '/clean/')
    os.makedirs(path + '/import/')
    os.makedirs(d)
    search(path + '/import/', ds)
    clean_h(path + '/import/0_homology_genes.tsv', path + '/clean/0_homology_genes.tsv')
    clean_g(path + '/clean/', path + '/import/')
    k_way(path + '/clean/')
    sp.run(args=['grimm_synt', '-A', '-f', f, '-d', d])
    f1 = path + '/clean/grimm_a_output/unique_coords.txt'
    for m in range(4, 16, 2):
        for g in range(2, 14, 2):
            os.makedirs(path + '/grimm_output/gene_m' + str(m) + '_g' + str(g))
            d1 = path + '/grimm_output/gene_m' + str(m) + '_g' + str(g)
            sp.run(args=['grimm_synt', '-f', f1, '-d', d1, '-c', '-p', '-m', str(m), '-g', str(g)])
    click.echo('Done in: ' + str(time.time() - start_time) + ' seconds.')