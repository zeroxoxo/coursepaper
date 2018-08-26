import math as m


def anch_denc():
    out = {}
    for t in range(4, 14, 2):
        for v in range(4, 10, 2):
            a = open('C:/Users/1/Desktop/Data/last_wf_out/grimm_output/gene_m' + str(t) + '_g' + str(v) + '/mgr_micro.txt', 'r')
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
            out['gene_m' + str(t) + '_g' + str(v)] = [xys, yzs, xzs]
    return out


print(anch_denc())
