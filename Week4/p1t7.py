import sys

for line in sys.stdin:
    val1, val2 =  line.strip().split(",")
    print(str(val2) + "\t1" )
