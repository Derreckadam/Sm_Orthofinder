#!/bin/bash

#SBATCH --nodes 1 --ntasks 1 --mem 2G --time 1:00:00 --out sfetch.out
module load hmmer

#do first time
#for i in /rhome/dcart001/shared/projects/Serratia/compare/150_genomes/orthofinder_in/*.fasta
#do
   # esl-sfetch --index $i
#done

while read line;do IFS=' ' list+=(${line}); done < sfetch_search_list.txt
num=${#list[@]}

count=0
while [ $count -lt $num ]; do
    if [ $((count%3)) -eq 0 ];
    then
        GCF1=${list[count]}
	GCF2="$GCF1*.fasta"
	WP=${list[count+1]}
	GCF3=`basename /rhome/dcart001/shared/projects/Serratia/compare/150_genomes/orthofinder_in/$GCF2`
	WP=\"$GCF1"|"$WP\"
	Ortho=${list[count+2]};
	fi
    
    echo esl-sfetch /rhome/dcart001/shared/projects/Serratia/compare/150_genomes/orthofinder_in/$GCF3 $WP \>\> $Ortho.fasta
    let count=count+3
done
