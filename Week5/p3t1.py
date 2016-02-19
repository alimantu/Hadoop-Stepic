import sys

for line in sys.stdin:
    print(line.strip())
    v, pr, out = line.strip().split("\t")
    if len(out) > 2:
        out = out[1:-1].split(",")
        cnt = len(out)
        pr = float(pr)
        for i in out:
            print(i + "\t" + ("%.3f" % (pr / cnt)) + "\t{}")
