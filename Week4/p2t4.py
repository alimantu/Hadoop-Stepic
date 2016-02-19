import sys

prevVal = ""
for line in sys.stdin:
    vals =  [i for i in line.strip().split("\t")]
    if prevVal != vals[0]:
        prevVal = vals[0]
    else:
        print(prevVal)
