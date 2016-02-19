import sys

for line in sys.stdin:
    vals =  line.strip().split(" ")
    for i in vals:
        for j in vals:
            if i != j:
                print(str(i) + "," + str(j) + "\t1")
