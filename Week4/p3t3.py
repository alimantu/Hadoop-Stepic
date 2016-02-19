import sys

prevVal = ""
cnt = 0
for line in sys.stdin:
    val = [str(i) for i in line.strip().split("\t")]
    print(val[0] + "\t" + ";".join(val[1:]) + ";1")
