from collections import Counter


def label_to_number(file): # 标签到数字的函数
    counter = Counter()
    revcounter = Counter()
    with open(file, 'r') as f:
        while True:
            line = list(f.readline().split())  # 逐行读取
            if not line:
                break
            counter[line[2].lower()] = line[1]
            revcounter[line[1]] = line[2].lower()
    return counter, revcounter


if __name__ == '__main__':
    f = open('vertex')

    f.close()