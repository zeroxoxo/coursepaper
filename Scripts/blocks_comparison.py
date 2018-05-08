import pandas as pd

def comparison(path):
    o = []
    for i in range(5):
        for g in range(5):
            x = pd.read_table(path + '/gene_m' + str(i+3) + '_g' + str(g+2) + '/blocks.txt', header=None, sep='\t')
            rows, col = x.shape
            o.append(str(rows-4) + ' m' + str(i+3) + ' g' + str(g+2))
    print(o)
    return
comparison('/home/lab51/coursepaper/Data/new_wf_out/grimm_output')

