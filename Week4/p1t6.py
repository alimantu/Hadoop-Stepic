import sys

prevVal = ""
for line in sys.stdin:
    val, tmp =  line.strip().split("\t")
    if (prevVal != val):
        print(val)
        prevVal = val
