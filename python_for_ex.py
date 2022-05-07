from sub_graph.minDFScode import search_minDFScode
import pandas as pd
from graph_similarity.SED import SEDist
from graph_dataset.vertex_to_label import label_to_number


def compute_similarity(code1, code2):
    """
    两个字符串的相似度
    :param: code1
    :param: code2
    :return: 两个字符串的编辑距离
    """
    return SEDist(code1, code2)


def test_is_right():
    """

    :return: 检验结果是否正确
    """

    print("hello world")


def one_node_recommendation(code):
    """
    给出第一个节点，推荐出候选节点
    :param code: 第一个节点标签
    :return: 可能的后续节点
    """
    df = pd.read_csv('one_node_pattern.csv')
    is_exist = False
    # 1.如果有相同的节点就推荐相同的
    for index, row in df.iterrows():
        if row["us"] == code:
            is_exist = True
            print(row["cns"], row["conf"])
    if is_exist:
        return
    # 2.没有相同的就推荐相似的
    for index, row in df.iterrows():
        similarity = compute_similarity(code, row["us"])
        if similarity < 5: # 暂定阈值是3
            print(row["cns"], row["conf"])


def graph_recommendation(code):
    """
    给出一个最小DFS code，推荐出候选节点
    :param: code
    :return: 候选节点
    """
    df = pd.read_csv('pattern_table.csv')
    is_exist = False
    for index, row in df.iterrows():
        if row["us"] == code:
            is_exist = True
            print(row["cns"], row["conf"])
    if is_exist:
        return
    threshold = len(code)
    most_similarity = code
    for index, row in df.iterrows():
        similarity = compute_similarity(code, row["us"])
        if similarity < threshold:
            threshold = similarity
            most_similarity = row["us"]


if __name__ == '__main__':

    with open('./processSnippets/process_example', 'r') as f:
        while True:
            line = list(f.readline().split())  # 逐行读取
            ver = "begin"
            graph = {}
            if not line:
                break
            while True:
                if not line:
                    break
                if ver == "begin":
                    ver = line[0]
                if line[0] in graph:
                    graph[line[0]].append(line[1])
                else:
                    graph[line[0]] = []
                    graph[line[0]].append(line[1])
                line = list(f.readline().split())
            min_code = search_minDFScode(graph, ver)
            graph_recommendation(min_code)


