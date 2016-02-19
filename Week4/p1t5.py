import sys

for line in sys.stdin:
    val1, val2 =  line.strip().split("\t")
    for i in val2.split(","):
        print(str(val1) + "," + str(i) + "\t1")
