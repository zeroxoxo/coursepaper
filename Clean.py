import copy
def clean1(file):
    f = open(file, 'r')
    l = []
    for line in f:
        l.append(line.split('\t'))
    m = copy.deepcopy(l)
    for i in m:
        for j in i:
            if ((j == '') or (j == '\n')) and l.count(i) > 0:
                l.remove(i)
    m = copy.deepcopy(l)
    for i in m:
        r = ''
        for j in m:
            if (i[0] == j[0]) and (i != j) and (l.count(i) > 0) and (l.count(j) > 0):
                l.remove(j)
                r = i[0]
        if i[0] == r:
            l.remove(i)
    p = ''

    for i in l:
        for j in i:
            p += j + '\t'
        p = p[:-1]
    g = open(file[:-4] + '_post_clean.txt', 'w')
    g.write(p)
    f.close()
    g.close()
    return

clean1('f1.txt')