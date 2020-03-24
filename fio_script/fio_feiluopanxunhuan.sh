#!/bin/bash

#block=$1  #128k 1M
#rw=$2     #read write randread randwrite
#dp=$3      #1 32 128
#size=$4    #1G
#engine=$5   #libaio sync
#COUNTS=$6    #1 2 3 4 5 6 


#fio --output=./${engine}_${block}_${rw}_${dp}_${size}_$COUNTS --name=$rw --filename=/data/files${COUNTS} --ioengine=$engine --size=$size --direct=1 --thread=1  --blocksize=$block --rw=$rw --iodepth=$dp --numjobs=1

fio -output=/home/feiluopanRW -name=test -filename=/media/hsu/testRW -ioengine=libaio -size=111G -direct=1 -thread=1  -blocksize=4k -rw=randwrite -iodepth=32 -numjobs=1
fio -output=/home/feiluopanRW -name=test -filename=/media/hsu/testRW -ioengine=libaio -size=111G -direct=1 -thread=1  -blocksize=4k -rw=randwrite -iodepth=32 -numjobs=1
rm -rf /media/hsu/testRW

blockarray=(4k 1M)
rwarray=(read write) ## randread randwrite
dparray=(1)
sizearray=(111G)
enginearray=(libaio sync)
countarray=(1 2 3)




for a in {0..1}
do 
	for b in {0..1}
	do
		for c in {0..0}
		do 
			for d in {0..0}
			do 
				for e in {0..1}
				do 
					for f in {0..2}
					do 
						#fio -output=/home/luopan/${blockarray[a]}_${rwarray[b]}_${dparray[c]}_${sizearray[d]}_${enginearray[e]} -name=${rwarray[b]} -filename=/dev/sdb -ioengine=${enginearray[e]} -size=${sizearray[d]} -direct=1 -thread=1  -blocksize=${blockarray[a]} -rw=${rwarray[b]} -iodepth=${dparray[c]} -numjobs=1
						fio -output=/home/feiluopan${blockarray[a]}_${rwarray[b]}_${dparray[c]}_${sizearray[d]}_${enginearray[e]}_${countarray[f]} -name=test -filename=/media/hsu/test${countarray[f]} -ioengine=${enginearray[e]} -size=${sizearray[d]} -direct=1 -thread=1  -blocksize=${blockarray[a]} -rw=${rwarray[b]} -iodepth=${dparray[c]} -numjobs=1
						sleep 10
						rm -rf /media/hsu/test${countarray[f]}
						sleep 10
					done
				done
			done
		done
	done
done 
