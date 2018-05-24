#!/usr/bin/env python3

import csv

with open('input.txt') as csvfile:
	input = csv.reader(csvfile,delimiter="\n")
	for i in input:
		orthogroup = str(i).strip("['']")+(".txt")
		outdir = "aa." + orthogroup
		with open(orthogroup) as csvfile:
        		reader = csv.reader(csvfile,delimiter="\n")
        		for row in reader:
                		if row != []:
					x = str(row)
					y= x.find(',')
					if y < 0:
						row = str(row).strip("['']")#.split("|")[0]
						with open(outdir, 'a') as z:
							z.write(row + '\n')
					else:
						row = x.replace(',','\n')
						row_new = row.strip("[' ']")#.split("|")[0]
						with open(outdir, 'a') as z:
                                                        z.write(row_new + '\n')
