import pandas as pd


if __name__ == '__main__':
    cont_list = []
    dic = {}
    with open('vertex', 'r') as f:
        while True:
            line = list(f.readline().split())  # 逐行读取
            if not line:
                break
            dic["label"] = line[1]
            dic["activity"] = line[2]
            length = len(line)
            real_activity = ""
            for i in range(3, length):
                real_activity += line[i]
                real_activity += ' '
            dic["real_activity"] = real_activity
            cont_list.append(dic)
            dic = {}
    df = pd.DataFrame(cont_list)
    print(df)
    df.to_csv('vertex.csv', index=["label", "activity", "real_activity"])