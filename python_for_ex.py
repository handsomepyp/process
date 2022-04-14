from collections import Counter

d = Counter()
for c in 'absdfe':
    d[c] += 1
print(d)