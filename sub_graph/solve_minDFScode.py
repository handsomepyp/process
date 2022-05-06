from collections import Counter
import pandas as pd


def label_to_number():
    counter = Counter()
    revcounter = Counter()
    with open('./../graph_dataset/vertex', 'r') as f:
        while True:
            line = list(f.readline().split())  # 逐行读取
            if not line:
                break
            counter[line[2].lower()] = line[1]
            revcounter[line[1]] = line[2].lower()
    return counter, revcounter


if __name__ == '__main__':
    counter, revcounter = label_to_number()
    cont_list = []
    with open('./new_data', 'r') as f:
        while True:
            line = list(f.readline().split())  # 逐行读取
            if not line:
                break
            if line[0] == 't': #
                minDFScode = []
                graph_id = line[2]
                node_tag = {}
                number_mindfscode = {}
                number_mindfscode["graph"] = graph_id
                while True:
                    li = list(f.readline().split())
                    if li[0] == 'v':
                        node_tag[li[1]] = li[2]
                    elif li[0] == 'e':
                        frm = li[1]
                        to = li[2]
                        frm_tag = revcounter[node_tag[frm]]
                        to_tag = revcounter[node_tag[to]]
                        s = '(' + frm + ',' + to + ',' + '1,' + frm_tag + ','\
                            + li[3] + ',' + to_tag + ')'
                        minDFScode.append(s)
                    elif li[0] == 'support': # support
                        dfscode = ""
                        for ele in minDFScode:
                            dfscode += ele
                        number_mindfscode["minDFScode"] = dfscode
                        cont_list.append(number_mindfscode)
                        break
    df = pd.DataFrame(cont_list, columns=["graph", "minDFScode"])
    df.to_csv("minDFScode.csv", index=False)