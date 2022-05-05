import pm4py

if __name__ == '__main__':
    bpmn_graph = pm4py.read_bpmn("./pre_process/dataset/ex08_writer0001.bpmn")


    from pm4py.objects.conversion.bpmn import converter as bpmn_converter

    net, im, fm = bpmn_converter.apply(bpmn_graph)

    # pm4py.view_petri_net(net, im, fm)

    # 转换成 Process Tree
    from pm4py.objects.conversion.wf_net import converter as wf_net_converter

    tree = wf_net_converter.apply(net, im, fm)
    # pm4py.view_process_tree(tree)

    from pm4py.objects.process_tree import semantics

    log = semantics.generate_log(tree, no_traces=100)
    mp, im, fm = pm4py.discover_dfg(log)

    pm4py.view_dfg(mp, im, fm)
