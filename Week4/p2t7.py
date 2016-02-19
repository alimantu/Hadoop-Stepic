import sys

prevUsr = ""
prevData = {}
for line in sys.stdin:
    user, vals =  line.strip().split("\t")
    vals = [i for i in vals.split(":")]
    if prevUsr != user:
        if len(prevData) > 0:
            for i in prevData["query"]:
                for j in prevData["url"]:
                    print(str(prevUsr) + "\t" + i + "\t" + j)
        prevUsr = user
        prevData["query"] = []
        prevData["url"] = []
    prevData[str(vals[0])].append(vals[1])

if len(prevData) > 0:
    for i in prevData["query"]:
        for j in prevData["url"]:
            print(str(prevUsr) + "\t" + i + "\t" + j)
