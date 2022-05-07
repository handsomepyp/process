import pandas as pd

global ver_label
global node_to_label
global label_to_node
global st
global code


def DFS(ver, graph):
    """
    :param ver: 当前搜索的点
    :param graph: 图的邻接表表示
    :return:
    """
    st[ver] = True
    global code, ver_label
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
        code += '(' + str(frm_label) + ',' + str(to_label) + ',1,'\
                      + frm + ',1,' + to + ')'
        DFS(next_ver, graph)


if __name__ == '__main__':

    one_node_list = []
    us_list = []

    with open('./finally_result', 'r') as f:
        while True:
            line = list(f.readline().split())
            if not line:
                break
            element = {}
            graph = {}
            st = {}
            ver = "begin"
            if len(line) == 1: # 上游子图是一个点
                element["us"] = line[0]
                line = list(f.readline().split())
                cns = ""
                for l in line:
                    cns += l + ' '
                element["cns"] = cns
                line = list(f.readline().split())
                element["conf"] = line[1]
                one_node_list.append(element)
            else: # 上游子图是一个图
                while True:
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
                    line = list(f.readline().split())
                    if line[0].isdigit():
                        break
                ver_label = 0
                node_to_label = {}
                label_to_node = {}
                code = ""
                DFS(ver, graph)
                element["us"] = code
                cns = ""
                for l in line:
                    cns += l + ' '
                element["cns"] = cns
                line = list(f.readline().split())
                element["conf"] = line[1]
                us_list.append(element)
    # DFS(ver, graph)
    df1 = pd.DataFrame(one_node_list)
    df2 = pd.DataFrame(us_list)
    df1.to_csv('one_node_pattern.csv', index=["us", "cns", "conf"])
    df2.to_csv('pattern_table.csv', index=["us", "cns", "conf"])



