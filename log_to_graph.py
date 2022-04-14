import pandas as pd
import os
import pm4py

xes_path = 'xesfile/'


def traverse_file(path):
    """traverse all files"""
    files = os.listdir(path)
    return files


def import_xes(file, number, tag, edges):
    dic = {}
    f = open("finally_result", mode="a")
    from pm4py.objects.log.importer.xes import importer as xes_importer
    log = xes_importer.apply(xes_path + file)
    logg = pm4py.read_xes(xes_path + file)
    print("logg = ", logg)
    mp = pm4py.discover_heuristics_net(logg)
    print(mp)
    pm4py.view_heuristics_net(mp)
    dfg, start_activities, end_activities = pm4py.discover_dfg(log)
    for key, val in enumerate(dict(dfg).items()):
        a1 = val[0][0]
        a2 = val[0][1]
        if a1 not in dic:
            dic[a1] = number
            number += 1

        if a2 not in dic:
            dic[a2] = number
            number += 1
    print(dic)
    f.write('t # ' + str(tag) + '\n')
    for k, v in dic.items():
        f.write('v ' + str(v) + ' ' + k.replace(' ', '') + '\n')
    for key, val in enumerate(dict(dfg).items()):
        a1 = val[0][0]
        a2 = val[0][1]
        f.write('e ' + str(dic[a1]) + ' ' + str(dic[a2]) + ' ' + str(edges) + '\n')
        edges += 1
    return number, edges


if __name__ == '__main__':
    """生成一系列的可被gSpan算法执行的图文件"""
    files = traverse_file(xes_path)
    number = 0
    tag = 0
    edges = 0
    for file in files:
        number, edges = import_xes(file, number, tag, edges)
        tag += 1

