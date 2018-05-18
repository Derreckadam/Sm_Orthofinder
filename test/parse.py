#!/usr/bin/env python3

import csv

orthofile = "input.txt"

with open('prod_producers.txt') as f:
    	prod_list = f.read().splitlines()
	
print "Looking for ", prod_list

with open(orthofile) as csvfile:
	reader = csv.reader(csvfile,delimiter="\t")
	for row in reader:
		ortho_name= row[0]
		sp_messy_name= row[1:4]
		sp_name=sp_messy_name.split("|")
		#need a way to delete everything after pipe character
		if set(prod_list) == set(sp_name):
			print ortho_name, sp_name 
