import os
import pm4py

xes_path = 'xes_log/'


def traverse_file(path):
    """traverse all files"""
    files = os.listdir(path)
    return files


def log_to_dfg(file, tag, edges):
    """
    日志 -> dfg直接跟随图
    :param file:
    :param tag:
    :param edges:
    :return:
    """
    dic = {}
    f = open("graph_dataset/graph_dataset", mode="a")
    from pm4py.objects.log.importer.xes import importer as xes_importer
    log = xes_importer.apply(xes_path + file)

    dfg, start_activities, end_activities = pm4py.discover_directly_follows_graph(log)
    number = 1
    for key, val in enumerate(dict(dfg).items()):
        a1 = val[0][0]
        a2 = val[0][1]
        if a1 not in dic:
            dic[a1] = number
            number += 1

        if a2 not in dic:
            dic[a2] = number
            number += 1
    for k, v in start_activities.items():
        if k not in dic:
            dic[k] = number
            number += 1
    for k, v in end_activities.items():
        if k not in dic:
            dic[k] = number
            number += 1

    f.write('t # ' + str(tag) + '\n')
    # 写入start point
    f.write('v 0 start\n')

    for k, v in dic.items():
        f.write('v ' + str(v) + ' ' + k.replace(' ', '') + '\n')
    # 写入end point
    f.write('v ' + str(number) + ' end\n')

    # 0 -> start(虚拟的边)
    for k, v in start_activities.items():
        f.write('e 0 ' + str(dic[k]) + ' ' + str(edges) + '\n')
        edges += 1

    # dfg图中的边
    for key, val in enumerate(dict(dfg).items()):
        a1 = val[0][0]
        a2 = val[0][1]
        f.write('e ' + str(dic[a1]) + ' ' + str(dic[a2]) + ' ' + str(edges) + '\n')
        edges += 1
    # end -> number(虚拟尾结点)
    for k, v in end_activities.items():
        f.write('e ' + str(dic[k]) + ' ' + str(number) + ' ' + str(edges) + '\n')
        edges += 1
    return number, edges


if __name__ == '__main__':
    input_files = traverse_file(xes_path)
    number = 0
    tag = 0
    edges = 0
    for file in input_files:
        number, edges = log_to_dfg(file, tag, edges)
        tag += 1
    f = open("graph_dataset/graph_dataset", mode="a")
    f.write("t # -1")
