from sub_graph.minDFScode import search_minDFScode
import pandas as pd
from graph_similarity.SED import SEDist
from graph_dataset.vertex_to_label import label_to_number
import time


def compute_similarity(code1, code2):
    """
    两个字符串的相似度
    :param: code1
    :param: code2
    :return: 两个字符串的编辑距离
    """
    return SEDist(code1, code2)


def test_is_right(node_list, line):
    """
    :param: 推荐结果列表
    :return: 检验结果是否正确
    """
    counter, revcounter = label_to_number('./graph_dataset/vertex')
    for index, row in node_list.iterrows():
        l = list(row["cns"].split())
        for number in l:
            print(revcounter(int(number)))
    print("hello world")


def one_node_recommendation(code):
    """
    给出第一个节点，推荐出候选节点
    :param code: 第一个节点标签
    :return: res 可能的后续节点
    """
    res = []
    df = pd.read_csv('one_node_pattern.csv')
    is_exist = False
    dic = {}
    # 1.如果有相同的节点就推荐相同的
    for index, row in df.iterrows():
        if row["us"] == code:
            is_exist = True
            dic["cns"] = row["cns"]
            dic["conf"] = row["conf"]
            res.append(dic)
            dic = {}
    if is_exist:
        return res
    # 2.没有相同的就推荐相似的
    for index, row in df.iterrows():
        similarity = compute_similarity(code, row["us"])
        if similarity < 5:  # 暂定阈值是3
            dic["cns"] = row["cns"]
            dic["conf"] = row["conf"]
            res.append(dic)
            dic = {}
    return res


def graph_recommendation(code):
    """
    给出一个最小DFS code，推荐出候选节点
    :param: code
    :return: res 所有的候选节点以及其置信度
    """
    res = []
    df = pd.read_csv('pattern_table.csv')
    is_exist = False
    dic = {}
    # 1.存在相同的图
    for index, row in df.iterrows():
        if row["us"] == code:
            is_exist = True
            dic["cns"] = row["cns"]
            dic["conf"] = row["conf"]
            res.append(dic)
            dic = {}
    if is_exist:
        return res
    threshold = len(code)
    most_similarity = code
    # 2.不存在相同的，只有相似的
    for index, row in df.iterrows():  # 找到最相似的子图
        similarity = compute_similarity(code, row["us"])
        if similarity < threshold:
            threshold = similarity
            most_similarity = row["us"]
    # most_similarity是最相似的子图，找到他所有的候选节点
    for index, row in df.iterrows():
        if most_similarity == row["us"]:
            dic["cns"] = row["cns"]
            dic["conf"] = row["conf"]
            dic = {}
            res.append(dic)
    return res


def top_k(all_node_list, k):
    """
    返回 topk 个候选节点组成的列表
    :param k:
    :return: DataFrame格式的 topk 个候选节点列表
    """
    unsorted_df = pd.DataFrame(all_node_list)
    sorted_df = unsorted_df.sort_values(by='conf', ascending=False)
    sorted_df.reset_index(drop=True, inplace=True)
    return sorted_df.loc[0:k - 1]


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
            # 返回后续节点列表

            start = time.process_time()
            res = graph_recommendation(min_code)
            # 返回 top-k
            node_list = top_k(res, 1)

            end = time.process_time()
            print("time consuming : {:.2f}s".format(end - start))
            print(node_list)
            # line = list(f.readline().split())
