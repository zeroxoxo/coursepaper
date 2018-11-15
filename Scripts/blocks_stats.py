import math as m
import pandas as pd

#path = 'C:/Users/1/Desktop/Data/last_wf_out'


def quick_stats(path):
    anc_used = 0
    anc_total = 1
    total_blocks = 0
    species = 1
    file_out = open(path + '/blocks_stats.tsv', 'a')
    file_out.write('m\tg\tAnchor Density\tCoverage\tNumber of blocks\n')
    for i in range(4, 16, 2):
        for j in range(2, 14, 2):
            file = open(path + '/grimm_output/gene_m' + str(i) + '_g' + str(j) + '/report.txt', 'r')
            lines = file.readlines()
            file.close()
            q = []
            for line in lines:
                if line[:12] == '  # species:':
                    species = int(line[23:])
                elif line[:12] == '  # anchors:':
                    anc_total = int(line[23:])
                elif line[:5] == 'block':
                    s = line.split()
                    p = lines[lines.index(line)+1].split()
                    p1 = p[2:]
                    p2 = []
                    for u in p1:
                        u = int(u)
                        p2.append(u)
                    q.append(int(s[2]) * (2 * species) / sum(p2))
                elif line[:6] == 'Totals':
                    s = line.split()
                    anc_used = int(s[1])
                    total_blocks = int(s[4])
            try:
                w = sum(q) / len(q)
            except ZeroDivisionError:
                w = 0
            file_out.write(str(i) + '\t' + str(j) + '\t' + str(round(w, 4)) + '\t' + str(round(anc_used / anc_total, 4)) +
                  '\t' + str(total_blocks) + '\n')
    file_out.close()
    return species


def anch_denc3(path):
    out = []
    for t in range(4, 16, 2):
        for v in range(2, 14, 2):
            a = open(path + '/grimm_output/gene_m' + str(t) + '_g' + str(v) + '/mgr_micro.txt', 'r')
            ar = a.readlines()
            datalayer0 = []
            datalayer1 = []
            for idx, line in enumerate(ar):
                l = line.split()
                try:
                    if l[1] == 'begin_block':
                        block = [int(l[4]), int(l[4])+int(l[5]), int(l[8]), int(l[8])+int(l[9]), int(l[12]), int(l[12])+int(l[13])]
                        datalayer1.append(block)
                    elif l[1] == 'begin_anchors':
                        xyz = []
                        for ln in range(idx + 1, len(ar)):
                            lne = ar[ln].split()
                            if lne[1] == 'end_anchors':
                                break
                            x = (int(lne[2]) * 2 + int(lne[3])) / 2
                            y = (int(lne[6]) * 2 + int(lne[7])) / 2
                            z = (int(lne[10]) * 2 + int(lne[11])) / 2
                            r = []
                            r.append(x)
                            r.append(y)
                            r.append(z)
                            xyz.append(r)
                        datalayer1.append(xyz)
                        datalayer0.append(datalayer1)
                        datalayer1 = []
                except Exception:
                    pass

            xys = 0
            yzs = 0
            xzs = 0
            for i in range(len(datalayer0)):
                b1 = 0
                b2 = 0
                b3 = 0
                x1 = datalayer0[i][0][0]
                x2 = datalayer0[i][0][1]
                y1 = datalayer0[i][0][2]
                y2 = datalayer0[i][0][3]
                z1 = datalayer0[i][0][4]
                z2 = datalayer0[i][0][5]
                a_num = len(datalayer0[i][1])
                for j in range(a_num):
                    xkj = datalayer0[i][1][j][0]
                    ykj = datalayer0[i][1][j][1]
                    zkj = datalayer0[i][1][j][2]
                    b1 += (x2 - x1) * (y1 - ykj) - (x1 - xkj) * (y2 - y1)
                    b2 += (y2 - y1) * (z1 - zkj) - (y1 - ykj) * (z2 - z1)
                    b3 += (x2 - x1) * (z1 - zkj) - (x1 - xkj) * (z2 - z1)
                xy = m.fabs(b1) / m.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
                yz = m.fabs(b2) / m.sqrt(((y2 - y1) ** 2) + ((z2 - z1) ** 2))
                xz = m.fabs(b3) / m.sqrt(((x2 - x1) ** 2) + ((z2 - z1) ** 2))
                xys += xy
                yzs += yz
                xzs += xz
            out.append(round((xys + yzs + xzs)/3, 4))
    return out

def anch_denc2(path):
    out = []
    for t in range(4, 16, 2):
        for v in range(2, 14, 2):
            a = open(path + '/grimm_output/gene_m' + str(t) + '_g' + str(v) + '/mgr_micro.txt', 'r')
            ar = a.readlines()
            datalayer0 = []
            datalayer1 = []
            for idx, line in enumerate(ar):
                l = line.split()
                try:
                    if l[1] == 'begin_block':
                        block = [int(l[4]), int(l[4])+int(l[5]), int(l[8]), int(l[8])+int(l[9])]
                        datalayer1.append(block)
                    elif l[1] == 'begin_anchors':
                        xy = []
                        for ln in range(idx + 1, len(ar)):
                            lne = ar[ln].split()
                            if lne[1] == 'end_anchors':
                                break
                            x = (int(lne[2]) * 2 + int(lne[3])) / 2
                            y = (int(lne[6]) * 2 + int(lne[7])) / 2
                            r = []
                            r.append(x)
                            r.append(y)
                            xy.append(r)
                        datalayer1.append(xy)
                        datalayer0.append(datalayer1)
                        datalayer1 = []
                except Exception:
                    pass

            xys = 0
            for i in range(len(datalayer0)):
                b1 = 0
                x1 = datalayer0[i][0][0]
                x2 = datalayer0[i][0][1]
                y1 = datalayer0[i][0][2]
                y2 = datalayer0[i][0][3]
                a_num = len(datalayer0[i][1])
                for j in range(a_num):
                    xkj = datalayer0[i][1][j][0]
                    ykj = datalayer0[i][1][j][1]
                    b1 += (x2 - x1) * (y1 - ykj) - (x1 - xkj) * (y2 - y1)
                xy = m.fabs(b1) / m.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
                xys += xy
            out.append(round(xys, 4))
    return out

def blocks_stats(path):
    species = quick_stats(path)
    if species == 2:
        lst = anch_denc2(path)
    elif species == 3:
        lst = anch_denc3(path)
    else:
        lst = []
        print('At this moment available only 2 or 3 species analysis')
    df = pd.read_table(path + '/blocks_stats.tsv', sep='\t')
    df1 = df.assign(Anchor_distance=lst)
    df1.to_csv(path + '/blocks_stats.tsv', sep='\t', index=False)
    return print('Done')

blocks_stats('C:/Users/1/Desktop/Data/achr_data/atr_alb')

