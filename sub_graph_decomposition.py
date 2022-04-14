import os
from collections import Counter

if __name__ == '__main__':
    file = open('./sub_graph/sub_graph_data')
    lines = file.readlines()
    h = Counter()
    dic = {}
    dic_all = Counter()
    for line in lines:
        substr = list(line.split())
        if substr[0] == 't' and substr[2] == '-1':
            break
        elif substr[0] == 'v':
            dic[substr[1]] = substr[2]
        elif substr[0] == 'e':
            l = []
            l.append(dic[substr[1]])
            l.append(dic[substr[2]])
            h[tuple(list(l))] += 1
            dic_all[dic[substr[1]]] += 1
        else:
            dic = {}
    for k, v in h.items():
        print(k, v / dic_all[k[0]])
    res = {}
    final_seq = []
    while 1:
        s = input()
        final_seq.append(s)
        if s == 'exit':
            break
        else:
            cnt = 0
            for k, v in h.items():
                if k[0] == s:
                    cnt += v
            for k, v in h.items():
                if k[0] == s:
                    res[k[1]] = v / cnt
            if not res:
                print("end point")
                break
            for k, v in res.items():
                print(k, v)
            res = {}
    for s in final_seq:
        print("{}->".format(s), end='')