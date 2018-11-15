import pandas as pd

path = r'C:\Users\1\Desktop\Data\gam_atr\grimm_output\gene_m8_g6\blocks.txt'
df = pd.read_table(path, header=None, skiprows=3, sep=' ')

df[3] = df[2] + df[3]
df[7] = df[6] + df[7]
df[1] = 'ag' + df[1]
df[5] = 'at' + df[5]

df1 = df.iloc[:, [1,2,3,5,6,7]]
l = []
sh  = df1.shape[0]
chr = []

for j in df1.iloc[:, 0]:
    if j not in chr:
        chr.append(j)

for i in range(sh):
    idx = chr.index(df1.iloc[i, 0])
    l.append('color=' + str(round(((i+1)*255/(idx+1))/sh)) + ',' + str(round(255/(idx+1)) - round(((i+1)*255/(idx+1))/sh)) + ',' + str(round(255/(idx+1))) + ',0.6')

df1[8] = l

df1.to_csv(r'C:\Users\1\Desktop\circos-0.69\bin\plot\data\blocks.txt', sep=' ', index=False, header=None)
