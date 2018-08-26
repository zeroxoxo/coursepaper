import pandas as pd

p = pd.read_table('C:/Users/1/Desktop/Data/last_wf_out/clean/grimm_a_output/unique_coords.txt', header=None)
r, c = p.shape
y = 0
for i in range(4, 14, 2):
    for j in range(4, 10, 2):
        file = open('C:/Users/1/Desktop/Data/last_wf_out/grimm_output/gene_m' + str(i) + '_g' + str(j) + '/report.txt', 'r')
        lines = file.readlines()
        file.close()
        q = []
        for line in lines:
            if line[:5] == 'block':
                s = line.split()
                p = lines[lines.index(line)+1].split()
                p1 = p[2:]
                p2 = []
                for u in p1:
                    u = int(u)
                    p2.append(u)
                q.append(int(s[2])*6 / sum(p2))
            elif line[:6] == 'Totals':
                s = line.split()
                y = int(s[1])
        w = sum(q) / len(q)
        print('gene_m' + str(i) + '_g' + str(j) + ': Anchor Density: ' + str(w) + ' Coverage: ' + str(y / r))