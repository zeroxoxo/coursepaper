from biomart import BiomartServer
server = BiomartServer('http://biomart.vectorbase.org/biomart/')
import click
@click.command()
@click.argument('ds', nargs=-1)
@click.argument('path', nargs=1, type=click.Path(exists=True))
def search(path, ds):
    for i in ds:
        r = server.datasets[i].search({
            'filters': {},
            'attributes': [ 'chromosome_name', 'start_position', 'end_position', 'strand', 'ensembl_gene_id' ]
        })
        name = path + i + '.txt'
        f = open(name, 'w')
        f.close()
        f = open(name, 'a')
        for line in r.iter_lines():
            line = line.decode('utf-8')
            f.write(line + '\n')
        f.close()
    click.echo('Done')

