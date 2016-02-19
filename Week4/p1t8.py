import sys

vals = {}
prevVal = ""
for line in sys.stdin:
    val1, val2 =  line.strip().split("\t")
    if line != prevVal:
        vals[str(val2)] = vals.get(str(val2), 0)
        vals[str(val2)] += 1
        prevVal = line

for (k, v) in vals.items():
    print(str(k) + "\t" + str(v))
