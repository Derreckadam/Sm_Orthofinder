#!/usr/bin/env python3

import csv
 
with open('Orthogroups.csv') as csvfile:
        reader = csv.reader(csvfile,delimiter="\t")
        for row in reader:
                ortho_name= row[0]
                sp_name=row[1:] 
		outdir = ortho_name + ".txt" 
		print ortho_name, "\n", "\n".join(sp_name)

		with open(outdir, 'w') as f:
    			for s in sp_name:
        			f.write(str(s) + '\n')
