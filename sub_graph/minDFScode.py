

def search_minDFScode(graph, ver):
    """
    有向图和初始节点返回其最小DFS编码
    :param ver: 起始节点
    :return: 有向图的最小DFS编码
    """
    st = {}
    code = ""
    node_to_label = {}
    label_to_node = {}
    ver_label = 0
    for key, val in graph.items():
        st[key] = False
        for v in val:
            st[v] = False

    def DFS(ver, graph):
        """
        :param ver: 当前搜索的点
        :param graph: 图的邻接表表示
        :return:
        """
        st[ver] = True
        nonlocal code, ver_label
        node_to_label[ver] = ver_label
        label_to_node[ver_label] = ver
        ver_label += 1
        if ver not in graph:
            return
        graph[ver].sort()
        for next_ver in graph[ver]:
            if st[next_ver]:
                break
            frm = ver
            to = next_ver
            frm_label = node_to_label[ver]
            to_label = ver_label
            code += '(' + str(frm_label) + ',' + str(to_label) + ',1,' \
                    + frm.lower() + ',1,' + to.lower() + ')'
            DFS(next_ver, graph)
    DFS(ver, graph)
    return code


if __name__ == '__main__':
    print("pypnb")