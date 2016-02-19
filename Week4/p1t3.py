import sys

prevUrl = ""
prevVals = []
for line in sys.stdin:
    url, val =  line.strip().split("\t")
    val = int(val)
    if url != prevUrl:
        if len(prevVals) != 0:
            print(str(prevUrl) + '\t' + str(int(sum(prevVals) / len(prevVals))))
        prevVals = [val]
        prevUrl = url
    else:
        prevVals.append(val)

if len(prevVals) != 0:
    print(str(prevUrl) + '\t' + str(int(sum(prevVals) / len(prevVals))))
