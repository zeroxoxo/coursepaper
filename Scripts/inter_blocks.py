import pandas as pd


def inter_blocks(path_a, path_b):
    i_num = []
    a = pd.read_table(path_a + '/blocks1.txt', header=None, sep=' ')
    b = pd.read_table(path_b + '/unique_coords1.txt', header=None, sep=' ')
    a_rows, a_cols = a.shape
    b_rows, b_cols = b.shape
    count = 0
    a[3] = a[2] + a[3]
    b[3] = b[2] + b[3]
    x = a.iloc[:, :4]
    y = b.iloc[:, :4]
    iter_rows = 0
    summ = 0
    while y[3][iter_rows] < x[2][0]:
        iter_rows += 1
        count += 1
    i_num.append(count)
    count = 0
    for i in range(a_rows - 1):
        for j in range(b_rows):
            if (y[2][j] > x[3][i]) and (y[3][j] < x[2][i + 1]) and (y[1][j] == x[1][i]):
                count += 1
        i_num.append(count)
        count = 0
    while y[2][b_rows - 1] > x[3][a_rows - 1]:
        b_rows -= 1
        count += 1
    i_num.append(count)
    for k in i_num:
        summ += k
    i_num.append(summ)
    out = pd.Series(i_num)
    out.to_csv(path_a + '/inter_blocks.txt', sep='\t')
    return


inter_blocks('C:/Users/1/Desktop/Data/wf_out2/clean/anch/gene_m3_g3', 'C:/Users/1/Desktop/Data/wf_out2/clean/anch')
