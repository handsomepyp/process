
if __name__ == '__main__':
    with open('./../processSnippets/process_example', 'r') as f:
        while True:
            line = list(f.readline().split())  # 逐行读取
            if not line:
                break
            print(line)
