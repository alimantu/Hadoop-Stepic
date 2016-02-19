import sys

prevUrl = ""
prevVals = []
prevCnt = 0
for line in sys.stdin:
    url, val =  line.strip().split("\t")
    val, cnt = val.split(";")
    val = int(val)
    if url != prevUrl:
        if len(prevVals) != 0:
            print(str(prevUrl) + '\t' + str(sum(prevVals)) + ';' + str(prevCnt))
        prevVals = [val]
        prevCnt = 1
        prevUrl = url
    else:
        prevVals.append(val)
        prevCnt += 1

if len(prevVals) != 0:
    print(str(prevUrl) + '\t' + str(sum(prevVals)) + ';' + str(prevCnt))
