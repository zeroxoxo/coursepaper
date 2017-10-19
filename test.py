from biomart import BiomartServer
server = BiomartServer( "http://biomart.vectorbase.org/biomart/" )
#'vb_gene_mart_1708': VectorBase Genes database
#'agambiae_eg_gene': Anopheles gambiae genes (AgamP4) dataset
#'agambiae_eg_genomic_sequence': Anopheles gambiae sequences (AgamP4)
# show server databases 'server.show_databases()'
# show server datasets 'server.show_datasets()'
# show all available filters and attributes of the 'uniprot' dataset:
# 'uniprot.show_filters()','uniprot.show_attributes()'
agambiae = server.datasets['agambiae_eg_gene'] #use 'a_gambiae' dataset
#'ensembl_gene_id': 'Gene stable ID', 'strand': 'Strand',
#'start_position': 'Gene start (bp)', 'end_position': 'Gene end (bp)'.
r = agambiae.search({
    'filters': {},
  'attributes': [ 'ensembl_gene_id', 'start_position', 'end_position', 'strand' ]
}, header = 1 )
file = open('test_response.txt', 'r')
# response format is TSV
for line in r.iter_lines():
  line = line.decode('utf-8')
  print(line.split("\t"))

file.close()