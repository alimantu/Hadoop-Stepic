import sys

prevVal = ""
flag = 2
for line in sys.stdin:
    vals =  [i for i in line.strip().split("\t")]
    if prevVal != vals[0]:
        if flag == 0:
            print(prevVal)
        flag = 0
        prevVal = vals[0]
    if vals[1] == "B":
        flag = 2

if flag == 0:
    print(prevVal)
