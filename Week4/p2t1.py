import sys

filterVal = "user10"
for line in sys.stdin:
    vals =  [i for i in line.strip().split("\t")]
    if vals[1] == filterVal:
        print("\t".join(vals))
