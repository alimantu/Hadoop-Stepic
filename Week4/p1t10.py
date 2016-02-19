import sys

for line in sys.stdin:
    vals =  line.strip().split(" ")
    for i in vals:
        stripe = {}
        for j in vals:
            if i != j:
                stripe[str(j)] = stripe.get(str(j), 0) + 1
        print(str(i) + "\t" + ",".join([str(k) + ":" + str(v) for (k, v) in stripe.items()]))
