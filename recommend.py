import os
import hashlib


def recommendNode(node): # 待推荐流程片段仅为一个节点
    """
    待推荐流程片段仅为一个节点
    :param node:
    :return:
    """
    print(node)


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


def recommendGraph(graph):
    """
    待推荐流程片段为一个子图
    :return:
    """
    print(graph)
    cur_graph_hash = str(hash_graph(graph))
    print(cur_graph_hash)
    h = {}
    with open('finally_result', 'r') as f:
        line1 = f.readline()
        line2 = f.readline()
        line3 = f.readline()
        while line1:
            if line1 == cur_graph_hash + '\n':
                h[line2] = line3
            line1 = f.readline()
            line2 = f.readline()
            line3 = f.readline()
    for k, v in h.items():
        print(k, v, end='')
    # print("hello world")


if __name__ == '__main__':
    file = open('./processSnippets/process_example')
    contents = file.readlines()
    flag = contents[0]
    if flag == "node\n":
        recommendGraph(contents[1])
    else:
        graph = []
        for content in contents:
            graph.append(list(content.split()))
        # print(graph)
        recommendGraph(graph)

