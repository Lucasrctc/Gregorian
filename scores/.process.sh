#!/bin/bash

filename=".temp.txt"
while read line; do
# reading each line
	cd ../tex
	./newchant.py $line ; line="tex/${line}.tex" ; cd ../ ; lualatex --shell-escape $line;
	./move.sh
	cd scores/
done < $filename
