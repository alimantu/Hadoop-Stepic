import sys

for line in sys.stdin:
    print(line.strip())
    v, w, out = line.strip().split("\t")
    if len(out) > 2:
        out = out[1:-1].split(",")
        for i in out:
            if w == "INF":
                print(i + "\tINF\t{}")
            else:
                print(i + "\t" + str(int(w) + 1) + "\t{}")
