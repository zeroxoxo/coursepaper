import pandas as pd
# script that makes annotation files of synthenic blocks for anopheles chromosomes
path = 'C:/Users/1/Desktop/Data/last_wf_out/grimm_output/gene_m12_g8'
table = pd.read_table(path + '/blocks.txt', header=None, sep=' ', skiprows=4)
rows, cols = table.shape
l = []
for row in range(rows):
    l.append('sb_' + str(row))
table[cols] = l
chrmsm = ['2L', '2R', '3L', '3R', 'X']
spec = ['a_gambiae', 'a_atroparvus', 'a_albimanus']
#anchors = pd.read_table('C:/Users/1/Desktop/Data/last_wf_out/clean/grimm_a_output/unique_coords.txt', header=None, sep=' ', skiprows=4)
for i in range(3):
    table1 = table.iloc[:, 1+(4*i):5+(4*i)]
    for n in chrmsm:
        table2 = table1.loc[table1[1+(4*i)] == n]
        table2[5+(4*i)] = table[cols]
        table2.iloc[:, 1:5].to_csv(path + '/ann_table_' + spec[i] + '_' + n + '.csv', sep=',', index=False)