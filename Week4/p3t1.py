import sys

punct = [":", ",", "\t", ".", "!", "?"]
for line in sys.stdin:
    ind = line.strip().index(":")
    docId = line.strip()[0:ind]
    vals = line.strip()[ind + 1:]
    for i in punct:
        vals = vals.replace(i, " ")
    for i in vals.split(" "):
        if i != "":
            print(str(i) + "#" + str(docId) + "\t1")
