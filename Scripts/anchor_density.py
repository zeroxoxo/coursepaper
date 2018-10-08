import pandas as pd

pan = pd.read_table('C:/Users/1/Desktop/Data/last_wf_out/clean/grimm_a_output/unique_coords.txt', header=None)
r, c = pan.shape
y = 0
tot = 0
for i in range(4, 16, 2):
    for j in range(2, 14, 2):
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
                tot = int(s[4])
        try:
            w = sum(q) / len(q)
        except ZeroDivisionError:
            w = 0
        print('gene_m' + str(i) + '_g' + str(j) + ': Anchor Density: ' + str(round(w, 4)) + ' Coverage: ' + str(round(y / r, 4)) +
              ' Number of blocks: ' + str(tot))