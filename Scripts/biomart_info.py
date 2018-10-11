from biomart import BiomartServer
server = BiomartServer('http://biomart.vectorbase.org/biomart/')
ds = server.datasets['aatroparvus_eg_gene']
fil = ds.show_filters()
print(fil)