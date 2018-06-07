#!/usr/bin/env python3

import csv
import os

non_prod_aa = '/rhome/dcart001/shared/projects/Serratia/compare/150_genomes/Sm_Orthofinder/transpose/'
for i in os.listdir(non_prod_aa):
    if 'aa.' in i:
        with open(i) as csvfile:
            reader = csv.reader(csvfile, delimiter='\n')
            for row in reader:
                row = str(row).strip("['']")
                rowsplit = row.split("|",1)
                GCF = rowsplit[0]
                if len(rowsplit) > 1:
                    ortho = str(i).strip("aa..txt")
                    print GCF, rowsplit[1], ortho
