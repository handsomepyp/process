import os
from collections import Counter


def label_to_number():
    counter = Counter()
    revcounter = Counter()
    with open('./graph_dataset/vertex', 'r') as f:
        while True:
            line = list(f.readline().split())  # 逐行读取
            if not line:
                break
            counter[line[2].lower()] = line[1]
            revcounter[line[1]] = line[2].lower()
    return counter, revcounter


class Pattern:
    """存储模式"""
    def __init__(self, Upstream_Subgraph, candidate_node_sets, support):
        self.Upstream_Subgraph = Upstream_Subgraph
        self.Candidate_Node_Sets = candidate_node_sets
        self.support = support


class pattern_List():
    """存储所有的模式（模式表）"""
    def __init__(self):
        self.list = []

    def add(self, pattern):
        self.list.append(pattern)


class UpstreamSubgraph():
    def __init__(self, Upstream_Subgraph):
        self.element = Upstream_Subgraph
        self.val = 0
        for edges in self.element:
            self.val += hash(tuple(edges))

class pattern_Table:
    """所有上游子图和support"""
    def __init__(self):
        self.Table = Counter()
        self.Tables = []

    def add(self, upstream, support):
        if self.Table[upstream.val]:
            self.Table[upstream.val] += int(support)
        else:
            self.Tables.append(upstream)
            self.Table[upstream.val] += int(support)


number_upstream_subgraph = Counter()
number_candidate_node_sets = Counter()
all_upstream_subpath = []
all_candidate_node_sets = []
pl = pattern_List()
pt = pattern_Table()


def decomposition(lines):
    number_to_label = {}
    st = set()
    edges = []
    node = []
    support = 0
    for line in lines:
        substr = list(line.split())
        # print(substr)
        if substr[0] == 't' and substr[2] == '0':
            continue
        elif substr[0] == 'v':
            number_to_label[substr[1]] = substr[2]
            node.append(substr[1])  # 添加一个节点
        elif substr[0] == 'e':
            edge = []
            edge.append(substr[1])
            edge.append(substr[2])
            edges.append(edge)
            st.add(substr[1])
        elif substr[0] == 'support':
            support = substr[1]
        else:
            # 针对第一个图，找到它的末尾节点
            candidate_node_sets_number = []
            candidate_node_sets = []
            upstream_subpath = []
            # 1. 找到所有的候选节点
            if len(node) > 1:
                for ver in node:
                    if ver not in st:
                        candidate_node_sets_number.append(ver)
                        candidate_node_sets.append(number_to_label[ver])
            # 2. 枚举所有的候选子图
            if len(edges) > 1:
                for edge in edges:
                    if edge[1] not in candidate_node_sets_number:
                        Edge = []
                        Edge.append(number_to_label[edge[0]])
                        Edge.append(number_to_label[edge[1]])
                        upstream_subpath.append(Edge)
            elif len(edges) == 1:
                upstream_subpath.append(number_to_label[edges[0][0]])
            else:
                upstream_subpath.append(number_to_label[node[0]])
            if len(upstream_subpath) == 0 and len(candidate_node_sets) != 0:
                for edge in edges:
                    if edge[0] not in candidate_node_sets_number and number_to_label[edge[0]] not in upstream_subpath:
                        upstream_subpath.append(number_to_label[edge[0]])
            # print(upstream_subpath, '->', end='')
            # print(candidate_node_sets, '->', end='')
            # print('support =', support)
            all_upstream_subpath.append(upstream_subpath)
            all_candidate_node_sets.append(candidate_node_sets)
            Pattern_add(upstream_subpath, candidate_node_sets, support)
            # 枚举下一个图，把一个图的信息清空
            number_to_label = {}
            node = []
            edges = []
            st = set()


def Pattern_add(upstream_subpath, candidate_node_sets, support):
    k = ()
    if not candidate_node_sets:
        return

    p = Pattern(upstream_subpath, candidate_node_sets, support)
    pl.add(p)
    val = UpstreamSubgraph(upstream_subpath)
    pt.add(val, support)
    # 改进pl, pt


def hash_graph(graph):
    """
    返回图的哈希值
    :param graph:
    :return: 图的哈希值
    """
    res = 0
    for edge in graph:
        res += hash(tuple(edge))
    return res


if __name__ == '__main__':
    counter, revcounter = label_to_number()
    file = open('./sub_graph/new_data')
    lines = file.readlines()
    file.close()
    decomposition(lines)
    elements = pl.list
    dic = pt.Table
    l = pt.Tables
    file = open('finally_result', mode="a")
    for element in elements:
        us = UpstreamSubgraph(element.Upstream_Subgraph)
        # print(element.Upstream_Subgraph, '->', element.Candidate_Node_Sets, '->', \
        #       'confidence', int(element.support) / dic[us.val])
        for edges in element.Upstream_Subgraph:
            for node in edges:
                file.write(revcounter[node] + ' ')
            file.write("\n")
        for ver in element.Candidate_Node_Sets:
            file.write(str(ver) + ' ')
        file.write('\n')
        file.write('confidence: ' + str(int(element.support) / dic[us.val]))
        file.write('\n')
