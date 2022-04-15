import os


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
    cur_graph_hash = hash_graph(graph)

    print("hello world")


if __name__ == '__main__':
    file = open('./processSnippets/process_example')
    contents = file.readlines()
    flag = contents[0]
    if flag == "node\n":
        recommendNode(contents[1])
    else:
        graph = []
        for content in contents:
            graph.append(list(content.split()))
        print(graph)
        recommendGraph(graph)
