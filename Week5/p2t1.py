n, m = input().split(" ")
n = int(n)
m = int(m)
ways = {}
for i in range(n):
    ways[i] = []
for i in range(m):
    f, t, w = input().split(" ")
    ways[int(f) - 1].append([int(t) - 1, int(w)])
init = [int(i) for i in input().split(" ")]

set2 = [i for i in range(n)]
set2.remove(init[0] - 1)
set1 = [init[0] - 1]
wSet1 = [0 for i in range(n)]

minV = -1
while init[1] - 1 not in set1:
    w = [0 for i in range(n)]
    used = [False for i in range(n)]
    for i in set1:
        for j in ways[i]:
            if j[0] in set2:
                if not used[j[0]] or w[j[0]] > (wSet1[i] + j[1]):
                    used[j[0]] = True
                    w[j[0]] = wSet1[i] + j[1]
    notSet = True
    minWay = 999
    minV = -1
    for i in set2:
        if used[i]:
            if notSet or minWay > w[i]:
                minWay = w[i]
                minV = i
                notSet = False
    if minV == -1:
        break
    else:
        set2.remove(minV)
        set1.append(minV)
        wSet1[minV] = minWay

if minV == -1:
    if init[0] != init[1]:
        print(-1)
    else:
        print(0)
else:
    print(wSet1[init[1] - 1])
