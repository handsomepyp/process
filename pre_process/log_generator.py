import pm4py
import os

# bpmn -> petri net -> process tree -> log(.xes) -> graph

src = 'dataset/'
res_path = 'new_log/'


def traverse_file(path):
    """
    :param path: src path
    :return: input file list
    """
    result_files = os.listdir(path)
    return result_files


def PT_generator_log(tree):
    from pm4py.objects.process_tree import semantics
    log = semantics.generate_log(tree, no_traces=100)
    return log


def petri_to_PT(net, im, fm):
    """
    生成流程树
    :param net:
    :param im:
    :param fm:
    :return: process tree
    """
    from pm4py.objects.conversion.wf_net import converter as wf_net_converter

    rtree = wf_net_converter.apply(net, im, fm)
    return rtree


def bpmn_to_petri(file):
    """
    生成Petri net
    :param files: 输入bpmn数据集列表
    :return: petri net
    """
    # 1.导入bpmn类型的数据集
    bpmn_graph = pm4py.read_bpmn(file)
    # 2.生成 Petri net
    from pm4py.objects.conversion.bpmn import converter as bpmn_converter

    net, im, fm = bpmn_converter.apply(bpmn_graph)
    return net, im, fm


if __name__ == '__main__':
    # 1.获取输入文件
    input_files = traverse_file(src)
    # 2.生成xes格式的流程日志
    for input_file in input_files:
        file = src + input_file
        final_name = input_file[0:15]
        # print(final_name)
        final_name += '.xes'
        result_files = os.listdir(res_path)
        # 2.1 生成Petri net
        net, im, fm = bpmn_to_petri(file)
        # 2.2 生成process tree
        tree = petri_to_PT(net, im, fm)
        # 2.3 生成日志
        log = PT_generator_log(tree)
        # 2.4 导出xes类型的文件
        from pm4py.objects.log.exporter.xes import exporter as xes_exporter

        print(input_file)
        xes_exporter.apply(log, res_path + final_name)