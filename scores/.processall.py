#! /usr/bin/env python3

import sys

sf = open("list.txt", "r")
x = sf.read()
sf.close()
df = open(".temp.txt", "w")
x = x.split('\n')
for i in x:
	if ".gabc" in i:
		i = i[:-5]
		count = 0
		print(i)
		sys.stdout.flush()
		df.write(str(i)+'\n')
df.close()
