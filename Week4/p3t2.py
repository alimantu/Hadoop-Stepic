import sys

prevVal = ""
cnt = 0
for line in sys.stdin:
    val, tmp = line.strip().split("\t")
    # val = [i for i in val.split("#")]
    if prevVal != val:
        if cnt > 0:
            print("\t".join([str(i) for i in prevVal.split("#")]) + "\t" + str(cnt))
        prevVal = val
        cnt = 0
    cnt += 1

if cnt > 0:
    print("\t".join([str(i) for i in prevVal.split("#")] + "\t" + str(cnt)))
