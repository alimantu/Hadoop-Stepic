import sys

for line in sys.stdin:
    vals =  [i for i in line.strip().split("\t")]
    print(vals[2])
