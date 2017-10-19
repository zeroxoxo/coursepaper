from biomart import BiomartServer
server = BiomartServer( "http://biomart.vectorbase.org/biomart/" )
import click
@click.command()
@click.option('--dataset','-ds', multiple=True)
@click.option('--path')
def search(dataset, path):
    x = server.datasets[dataset].search({
        'filters': {},
        'attributes': [ 'chromosome_name', 'start_position', 'end_position', 'strand', 'ensembl_gene_id' ]
    })
    name = path + dataset + '.txt'
    f = open(name, 'w')
    f.close()
    f = open(name, 'a')
    for line in r.iter_lines():
        line = line.decode('utf-8')
        print(line.split("\t"))
    f.close()
    click.echo('Done')
