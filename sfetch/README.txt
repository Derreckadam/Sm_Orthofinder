1. first parse data from Orthogroups.csv using 01_transpose.py
2. then 02_pull_non_prod_ortho.py will parse non-prodigiosin-proteins from input.txt genomes, these are placed in aa.ORTHOGROUP.txt
3. then 03_prep_sfetch_search.py > sfetch_search_list.txt will generate a list that you will use to iterate through data
4. 04_sfetch.sh will generate aa sequences for each orthogroup and place them in a new file called ORTHOGROUP.fasta
5. 05_to_do_list.sh will run each sfetch line and dump results into ORTHOGROUP.fasta
