import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

path = 'C:/Users/1/Desktop/Data/'
sp = ['gam_atr', 'gam_alb', 'atr_alb']
#sp = ['gam_atr']
sp_list = []
for idx, l in enumerate(sp):
    list_of_lists = []
    for j in range(4, 16, 2):
        for k in range(2, 14, 2):
            try:
                df = pd.read_table(path + l + '/grimm_output/gene_m'+str(j)+'_g'+str(k)+'/blocks.txt', sep=' ', header=None, skiprows=3)
                df[9] = (df[3] + df[7])/2
            except Exception as e:
                df = pd.DataFrame([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], columns=[0,1,2,3,4,5,6,7,8,9])
            lengths = [0, 0, 0, 0, 0, 0]
            all = 0
            for i in df[9]:
                all+=1
                if i <= 10000:
                    lengths[0] += 1
                elif i <= 50000:
                    lengths[1] += 1
                elif i <= 100000:
                    lengths[2] += 1
                elif i <= 500000:
                    lengths[3] += 1
                elif i <= 1000000:
                    lengths[4] += 1
                else:
                    lengths[5] += 1
            lengths.append(l + '_m'+str(j)+'_g'+str(k))
            list_of_lists.append(lengths)

    df_a = pd.DataFrame(list_of_lists)
    df_a.rename(columns={0:'10000', 1:'50000', 2:'100000', 3:'500000', 4:'1000000', 5:'else', 6:'parameters'}, inplace=True)
    df_a.set_index('parameters', inplace=True)
    sp_list.append(df_a)

gene = 8
print()
color_val = ['b', 'r', 'c']
xpos = np.arange(len(sp_list[0].columns.values))
plt.xticks(xpos, sp_list[0].columns.values)
for y in range(3):
    plt.bar(xpos - (y-1)*0.3, sp_list[y].iloc[gene, :].tolist(), label=sp[y], color=color_val[y], width=0.3)
plt.title('Number of blocks & Lengths for ' + sp_list[0].iloc[gene, :].name[8:])
plt.legend()
plt.show()
