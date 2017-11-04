from biomart import BiomartServer
server = BiomartServer('http://biomart.vectorbase.org/biomart/')
import click
@click.command()
@click.argument('ds', nargs=-1)
@click.argument('path', nargs=1, type=click.Path(exists=True))
def search(path, ds):
    for i in ds:
        r = server.datasets[i + '_eg_gene'].search({
            'filters': {},
            'attributes': [ 'chromosome_name', 'start_position', 'end_position', 'strand', 'ensembl_gene_id' ]
        })
        name = path + i + '_gene.txt'
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
    name1 = path + ds[0] + '_homology_genes.txt'
    f = open(name1, 'w')
    f.close()
    f = open(name1, 'a')
    for line in s.iter_lines():
        line = line.decode('utf-8')
        f.write(line + '\n')
    f.close()

    click.echo('Done')

