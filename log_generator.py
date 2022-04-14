import pandas
import pm4py
import os

bpmn_src = 'dataset/'


def import_csv():
    print("import csv")


def import_bpmn(bpmn_path):
    """import bpmn"""
    bpmn_graph = pm4py.read_bpmn(bpmn_path)
    # print(bpmn_graph)
    return bpmn_graph


def log_generator(tree):
    from pm4py.objects.process_tree import semantics

    log = semantics.generate_log(tree, no_traces=1)

    return log


def bpmn_to_petri(bpmn_graph):
    """bpmn to petri"""
    from pm4py.objects.conversion.bpmn import converter as bpmn_converter

    net, im, fm = bpmn_converter.apply(bpmn_graph)

    return net, im, fm


def petri_to_PT(net, im, fm):
    """petri net to process tree"""
    from pm4py.objects.conversion.wf_net import converter as wf_net_converter

    tree = wf_net_converter.apply(net, im, fm)

    return tree


def log_to_csv(log, name):
    from pm4py.objects.conversion.log import converter as log_converter
    dataframe = log_converter.apply(log, variant=log_converter.Variants.TO_DATA_FRAME)
    dataframe.to_csv(name)


def log_to_xes(log, name):
    from pm4py.objects.log.exporter.xes import exporter as xes_exporter
    xes_exporter.apply(log, name)


def bpmn_to_log(bpmn_file, name):
    """core function bpmn_file -> log_file"""
    bpmn_graph = import_bpmn(bpmn_file)
    net, im, fm = bpmn_to_petri(bpmn_graph)
    tree = petri_to_PT(net, im, fm)
    log = log_generator(tree)
    log_to_csv(log, name)


def bpmn_to_log_xes(bpmn_file, name):
    bpmn_graph = import_bpmn(bpmn_file)
    net, im, fm = bpmn_to_petri(bpmn_graph)
    tree = petri_to_PT(net, im, fm)
    log = log_generator(tree)
    log_to_xes(log, name)


def traverse_file(path):
    """traverse all files"""
    files = os.listdir(path)
    return files


def bpmn_to_csv():
    files = traverse_file(bpmn_src)
    for i in range(len(files)):
        if i == 7 or i == 9 or i == 10:  # 7,9,10不是工作流网
            continue
        file = bpmn_src + files[i]
        name = 'ex_' + str(i) + '_log.csv'
        name = 'logfile/' + name
        bpmn_to_log(file, name)


def bpmn_to_xes():
    files = traverse_file(bpmn_src)
    for i in range(len(files)):
        if i == 7 or i == 9 or i == 10:  # 7,9,10不是工作流网
            continue
        file = bpmn_src + files[i]
        name = 'ex_' + str(i) + '_log.xes'
        name = 'xes_file/' + name
        bpmn_to_log_xes(file, name)


if __name__ == '__main__':
    """main function"""
    bpmn_to_xes()