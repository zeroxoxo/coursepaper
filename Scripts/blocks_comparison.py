import pandas as pd

def comparison(path):
    o = []
    for i in range(9):
        x = pd.read_table(path + '/gene' + str(i+2) + '/blocks.txt',header=None, sep='\t')
        rows, col = x.shape
        o.append(rows)
    print(o)
    return
comparison('/home/lab51/coursepaper/Data/wf_out1/clean/anch')

