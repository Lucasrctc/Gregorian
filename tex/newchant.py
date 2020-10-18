#! /usr/bin/env python3

import sys

score = str(sys.argv[1])
newChant = score.replace("-", " ")
sf = open("test.tex", "r")
df = open(score+".tex", "w")

cont = sf.read()

sf.close()
beg = cont[:cont.find("NewChant")]
end = cont[cont.find("NewChant")+8:]
mid = end[:end.find("NewChant")]
end = end[end.find("NewChant")+8:]
x = (beg+newChant+mid+score+end)
x = x.split('\n')
for i in x:
    print(i)
df.write(beg+newChant+mid+score+end)
df.close()
