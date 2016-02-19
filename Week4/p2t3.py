import sys

prevVal = ""
for line in sys.stdin:
    vals =  [i for i in line.strip().split("\t")]
    if vals[0] != prevVal:
        print(vals[0])
        prevVal = vals[0]
