import time, click, os
import pandas as pd
from biomart import BiomartServer
import subprocess as sp

start_time = time.time()


@click.command()
@click.argument('ds', nargs=-1)
@click.argument('path', nargs=1, type=click.Path(exists=True))
def workflow(ds: str, path: str):
    file = f'{path}/clean/k_way_anchors.tsv'
    dir_ = f'{path}/clean/grimm_a_output'
    try:
        os.makedirs(path + '/clean/')
        os.makedirs(path + '/import/')
        os.makedirs(dir_)
    except Exception as e:
        print(e)
    # Start vb_request   
    vb_request(f'{path}/import/', ds)
    
    # Clean files
    clean_h(f'{path}/import/homology_genes.tsv', f'{path}/clean/homology_genes.tsv')
    clean_g(f'{path}/clean/', f'{path}/import/')
    
    # Prepare input file for GRIMM_Synteny
    k_way(f'{path}/clean/')
    
    # Run GRIMM_Synteny for anchors
    sp.run(args=['grimm_synt', '-A', '-f', file, '-d', dir_])
    
    f1 = f'{path}/clean/grimm_a_output/unique_coords.txt'
    # Shuffle through parameteres of minimum block size and maximum gap size, and get GRIMM_Synteny for them
    for m in range(4, 16, 2):
        for g in range(2, 14, 2):
            os.makedirs(f'{path}/grimm_output/gene_m{m}_g{g}')
            d1 = path + '/grimm_output/gene_m' + str(m) + '_g' + str(g)
            sp.run(args=['grimm_synt', '-f', f1, '-d', f'{path}/grimm_output/gene_m{m}_g{g}',
                         '-c', '-p', '-m', str(m), '-g', str(g)])
    click.echo(f'Done in: {time.time() - start_time} seconds.')


def vb_request(path: str, ds: tuple):
    "Access VectorBase API to get gene positions of requested species"
    # Init server
    server = BiomartServer('http://biomart.vectorbase.org/biomart/')
    # Iterate over requests for gene positions of requested species
    attr = ('chromosome_name', 'start_position', 'end_position', 'strand', 'ensembl_gene_id')
    for i,n in enumerate(ds):
        name = f'{path}/{i}_gene.tsv'
        with open(name, 'a') as f:
            rqst = server.datasets[n + '_eg_gene'].search({
                'filters': {},
                'attributes': attr
            })
            for line in rqst.iter_lines():
                f.write(line.decode('utf-8') + '\n')

    # Request for orthologous genes of requested species
    attr = ['ensembl_gene_id'] + [f'{ds[i]}_eg_homolog_ensembl_gene' for i in range(1, len(ds))]
    name = path + 'homology_genes.tsv'
    with open(name, 'w') as f:
        s = server.datasets[ds[0]+'_eg_gene'].search({
            'filters': {},
            'attributes': attr
        }, header = 1)
        for line in s.iter_lines():
            f.write(line.decode('utf-8') + '\n')
    return print('VB done.')

def clean_h(input_file: str, output_file: str):
    "Clean homology_genes.tsv file from empty cells and duplicates"
    # Open file
    in_file = pd.read_table(input_file, sep='\t', skiprows=1, header=None)
    # Drop rows with empty cells
    in_file.dropna(inplace=True)
    # Drop rows, where there is at least one duplicate value
    cols = in_file.shape[1]
    for i in range(cols):
        in_file.drop_duplicates(subset=[i], keep=False, inplace=True)
    # Write file
    in_file.to_csv(output_file, sep='\t', index=False, header=None)
    return print('Done Clean_h')

def clean_g(homology_path: str, genes_path: str):
    "Clean i_gene.tsv files"
    # Open homology_genes.tsv for reference
    ref = pd.read_table(f'{homology_path}homology_genes.tsv', sep='\t', header=None)
    cols = ref.shape[1]
    # For each column in reference leave only rows in i_genes.tsv that are present in reference
    for i in range(col):
        gene_input = pd.read_table(f'{genes_path}{i}_gene.tsv', sep='\t', header=None)
        gene_output = gene_input.loc[gene_input[4].isin(ref[i])]
        #gene_output = gene_input.loc[gene_input[gene_input.columns[4]].isin(ref[ref.columns[i]])]
        gene_output.to_csv(f'{homology_path}{i}_clean_genes.tsv', sep='\t', header=False, index=False)
    return print('Done Clean_g')

def k_way(path: str):
    "Form file to input to GRIMM_Synteny in k_way format, specified in README of GRIMM"
    ref = pd.read_table(path + 'homology_genes.tsv', header=None, sep='\t')
    rows, col = ref.shape
    labels = ('chr', 'start', 'len', 'sign')
    out = pd.Series([out for out in range(rows)], name='id')
    for i in range(col):
        genes = pd.read_table(f'{path}{i}_clean_genes.tsv', header=None, sep='\t')
        way = pd.merge(ref, genes, how='inner', left_on=ref.iloc[:,i], right_on=genes.iloc[:, 4], validate='one_to_one')
        way[2] = way[2] - way['1_y']
        way.columns = [f'genome{i+1}_{label}' for label in labels]
        #way.rename({'0_y': 'genome'+str(i+1)+'_chr', '1_y': 'genome'+str(i+1)+'_start', 2: 'genome'+str(i+1)+'_len',
        #                  3 : 'genome'+str(i+1)+'_sign'}, axis='columns', inplace=True)
        out = pd.concat([out, way.iloc[:,col:col+4]], join='inner', axis=1)
    out.to_csv(f'{path}k_way_anchors.tsv', sep='\t', index=False)
    return

