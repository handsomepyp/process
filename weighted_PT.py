import pandas as pd
import pm4py
import os

log_src = 'logfile/'


def traverse_file(path):
    """traverse all files"""
    files = os.listdir(path)
    return files


def weighted_PT(file):
    event_log = pm4py.format_dataframe(pd.read_csv(log_src + file, sep=','))
    pt = \
        pm4py.discover_bpmn_inductive(event_log)
    pm4py.view_bpmn(pt)
    print(pt)


if __name__ == '__main__':
    files = traverse_file(log_src)
    for file in files:
        weighted_PT(file)
