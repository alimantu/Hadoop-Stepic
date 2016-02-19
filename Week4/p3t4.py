import sys

def printVals(prevWord, prevVals):
    if len(prevVals) > 0:
        size = len(prevVals)
        for i in prevVals:
            tmp = i.split(";")
            print(str(prevWord) + "#" + str(tmp[0]) + "\t" + str(tmp[1]) + "\t" + str(size))

prevWord = ""
prevVals = []
for line in sys.stdin:
    word, vals = line.strip().split("\t")
    if prevWord != word:
        printVals(prevWord, prevVals)
        prevWord = word
        prevVals = []
    prevVals.append(vals)

printVals(prevWord, prevVals)
