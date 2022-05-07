from graph_dataset.vertex_to_label import label_to_number
import pandas as pd


def one_node_recommend(node):
    df = pd.read_csv('')


def graph_recommend():



if __name__ == '__main__':
    counter, revcounter = label_to_number('./../graph_dataset/vertex')
    with open('./testdata', 'r') as f:
        while True:
            line = list(f.readline().split())  # 逐行读取
            if not line:
                break
            if line[0] == 't' or line[2] == '-1':
                break
            graph = {}
            ver = "begin"
            st = {}
            while True:
                line = list(f.readline().split())  # 逐行读取
                if len(line) == 1:
                    one_node_recommend(line[0])
                if line[0] == 'result:':
                    for

                    break
                else:
                    if ver == "begin":
                        ver = line[0]
                    if line[0] in graph:
                        graph[line[0]].append(line[1])
                        st[line[0]] = False
                        st[line[1]] = False
                    else:
                        graph[line[0]] = []
                        graph[line[0]].append(line[1])
                        st[line[0]] = False
                        st[line[1]] = False
    print("hello world")