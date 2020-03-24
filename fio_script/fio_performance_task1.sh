#!/bin/bash

#block=$1  #128k 1M
#rw=$2     #read write randread randwrite
#dp=$3      #1 32 128
#size=$4    #1G
#engine=$5   #libaio sync
#COUNTS=$6    #1 2 3 4 5 6 


#fio --output=./${engine}_${block}_${rw}_${dp}_${size}_$COUNTS --name=$rw --filename=/data/files${COUNTS} --ioengine=$engine --size=$size --direct=1 --thread=1  --blocksize=$block --rw=$rw --iodepth=$dp --numjobs=1

time fio -output=/home/hsu/Desktop/fio_result/ -name=test -filename=/dev/sda -ioengine=libaio -size=63G -direct=1 -thread=1 -blocksize=4k -rw=write -iodepth=32 -numjobs=1


# # rm -rf /media/hsu/testRW

blockarray=(1k 4k 8k 16k 32k 64k 128k 1024k)
rwarray=(write)  ## randread randwrite
dparray=(32)
sizearray=(63G)
enginearray=(libaio)
countarray=(1)

for a in {0..7}
do 
	for b in {0..0}
	do
		for c in {0..0}
		do 
			for d in {0..0}
			do 
				for e in {0..0}
				do 
					for f in {0..0}
					do 
						#fio -output=/home/luopan/${blockarray[a]}_${rwarray[b]}_${dparray[c]}_${sizearray[d]}_${enginearray[e]} -name=${rwarray[b]} -filename=/dev/sdb -ioengine=${enginearray[e]} -size=${sizearray[d]} -direct=1 -thread=1  -blocksize=${blockarray[a]} -rw=${rwarray[b]} -iodepth=${dparray[c]} -numjobs=1
						time fio -output=/home/hsu/Desktop/fio_result/${blockarray[a]}_${rwarray[b]}_${dparray[c]}_${sizearray[d]}_${enginearray[e]}_${countarray[f]} -name=test -filename=/dev/sda -ioengine=${enginearray[e]} -size=${sizearray[d]} -direct=1 -thread=1  -blocksize=${blockarray[a]} -rw=${rwarray[b]} -iodepth=${dparray[c]} -numjobs=1 -runtime=600						
						sleep 10
						#rm -rf /media/hsu/test${countarray[f]}
						#sleep 10
					done
				done
			done
		done
	done
done 
###############################################################################################################
blockarray=(4k)
rwarray=(randwrite)  ## randread randwrite
dparray=(32)
sizearray=(63G)
enginearray=(libaio)
countarray=(1)

for a in {0..0}
do 
	for b in {0..0}
	do
		for c in {0..0}
		do 
			for d in {0..0}
			do 
				for e in {0..0}
				do 
					for f in {0..0}
					do 
						#fio -output=/home/luopan/${blockarray[a]}_${rwarray[b]}_${dparray[c]}_${sizearray[d]}_${enginearray[e]} -name=${rwarray[b]} -filename=/dev/sdb -ioengine=${enginearray[e]} -size=${sizearray[d]} -direct=1 -thread=1  -blocksize=${blockarray[a]} -rw=${rwarray[b]} -iodepth=${dparray[c]} -numjobs=1
						time fio -output=/home/hsu/Desktop/fio_result/${blockarray[a]}_${rwarray[b]}_${dparray[c]}_${sizearray[d]}_${enginearray[e]}_${countarray[f]} -name=test -filename=/dev/sda -ioengine=${enginearray[e]} -size=${sizearray[d]} -direct=1 -thread=1  -blocksize=${blockarray[a]} -rw=${rwarray[b]} -iodepth=${dparray[c]} -numjobs=1 -runtime=14400						
						sleep 10
						# rm -rf /media/hsu/test${countarray[f]}
						#sleep 10
					done
				done
			done
		done
	done
done 
###########################################################################################
blockarray=(1k 4k 8k 16k 32k 64k 128k 1024k)
rwarray=(randwrite write)  ## randread randwrite
dparray=(32)
sizearray=(63G)
enginearray=(libaio)
countarray=(2)


for a in {0..7}
do 
	for b in {0..1}
	do
		for c in {0..0}
		do 
			for d in {0..0}
			do 
				for e in {0..0}
				do 
					for f in {0..0}
					do 
						#fio -output=/home/luopan/${blockarray[a]}_${rwarray[b]}_${dparray[c]}_${sizearray[d]}_${enginearray[e]} -name=${rwarray[b]} -filename=/dev/sdb -ioengine=${enginearray[e]} -size=${sizearray[d]} -direct=1 -thread=1  -blocksize=${blockarray[a]} -rw=${rwarray[b]} -iodepth=${dparray[c]} -numjobs=1
						time fio -output=/home/hsu/Desktop/fio_result/${blockarray[a]}_${rwarray[b]}_${dparray[c]}_${sizearray[d]}_${enginearray[e]}_${countarray[f]} -name=test -filename=/dev/sda -ioengine=${enginearray[e]} -size=${sizearray[d]} -direct=1 -thread=1  -blocksize=${blockarray[a]} -rw=${rwarray[b]} -iodepth=${dparray[c]} -numjobs=1 -runtime=600
						#sleep 10
						# rm -rf /media/hsu/test${countarray[f]}
						# sleep 10
					done
				done
			done
		done
	done
done 