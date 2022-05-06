import os
import pm4py
from collections import Counter

xes_path = 'new_log/'


def traverse_file(path):
    """traverse all files"""
    files = os.listdir(path)
    return files


def label_to_number():
    counter = Counter()
    with open('./../graph_dataset/vertex', 'r') as f:
        while True:
            line = list(f.readline().split())  # 逐行读取
            if not line:
                break
            counter[line[2].lower()] = line[1]
    print(counter)
    return counter


def log_to_seq(file, counter):
    """
    把一个日志变成一个有序序列
    :param file:输入文件名
    :param counter:字典
    :return:
    """
    from pm4py.objects.log.importer.xes import importer as xes_importer
    logs = xes_importer.apply(xes_path + file)
    seq = []
    for log in logs:
        s = []
        for activity in log:
            strings = activity['concept:name'].replace(' ', '').lower()
            if strings in counter:
                s.append(counter[strings])
        if s:
            seq.append(s)
    print(seq)
    return seq


if __name__ == '__main__':
    counter = label_to_number()
    input_files = traverse_file(xes_path)
    k = 0
    S = [] # S代表所有日志轨迹
    for file in input_files:
        seq = log_to_seq(file, counter)
        S.append(seq)

