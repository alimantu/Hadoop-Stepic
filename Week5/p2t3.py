import sys

def printValues(v, mW, to):
    if v != "":
        print(v + "\t" + str(mW) + "\t" + to)

def getWeight(weight, prevWeight):
    if weight == "INF":
        return prevWeight
    if prevWeight == "INF":
        return int(weight)
    return min(int(weight), prevWeight)

prevV = ""
prevMinWeight = "INF"
prevTo = "{}"
for line in sys.stdin:
    v, w, out = line.strip().split("\t")
    if v != prevV:
        printValues(prevV, prevMinWeight, prevTo)
        prevV = v
        prevMinWeight = getWeight(w, "INF")
        prevTo = out
    else:
        prevMinWeight = getWeight(w, prevMinWeight)
        if len(out) > len(prevTo):
            prevTo = out
printValues(prevV, prevMinWeight, prevTo)
