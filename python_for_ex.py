
if __name__ == '__main__':
    f = open('python_for_ex')
    line = f.readline()
    print(line.isdigit())
    if type(line) == 'int':
        print("ok")