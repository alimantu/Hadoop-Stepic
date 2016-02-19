import sys

def printRes(v, pr, out):
    if v != "":
        print(v + "\t" + ("%.3f" % pr) + "\t" + out)

prevV = ""
prevPr = 0
prevOut = ""
for line in sys.stdin:
    v, pr, out = line.strip().split("\t")
    if prevV != v:
        printRes(prevV, prevPr, prevOut)
        prevV = v
        prevPr = 0
        prevOut = "{}"
    if len(out) > 2:
        prevOut = out
    else:
        prevPr += float(pr)
printRes(prevV, prevPr, prevOut)
