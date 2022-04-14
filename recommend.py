import os

if __name__ == '__main__':
    a = ['a', 'b']
    b = ['b', 'a']
    print(hash(tuple(a)), hash(tuple(b)))


