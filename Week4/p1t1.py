import sys

for line in sys.stdin:
    tokenList = {}
    for i in line.strip().split(" "):
        tokenList[i] = tokenList.get(i, 0) + 1
    for (k, v) in tokenList.items():
        print(str(k) + "\t" + str(v))
