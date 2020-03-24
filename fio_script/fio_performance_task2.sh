#!/bin/bash

#block=$1  #128k 1M
#rw=$2     #read write randread randwrite
#dp=$3      #1 32 128
#size=$4    #1G
#engine=$5   #libaio sync
#COUNTS=$6    #1 2 3 4 5 6 


#fio --output=./${engine}_${block}_${rw}_${dp}_${size}_$COUNTS --name=$rw --filename=/data/files${COUNTS} --ioengine=$engine --size=$size --direct=1 --thread=1  --blocksize=$block --rw=$rw --iodepth=$dp --numjobs=1
# time fio -output=/home/hsu/Desktop/fio_result/ -name=test -filename=/dev/sda -ioengine=libaio -size=63G -direct=1 -thread=1 -blocksize=4k -rw=write -iodepth=32 -numjobs=1
# # rm -rf /media/hsu/testRW


#-------------------------------------------------------------------------------------------------------------------------
time fio -output=/home/hsu/Desktop/fio_result/4k_randwrite_32_63G_libaio_1 -name=test -filename=/dev/sda -ioengine=libaio -size=63G -direct=1 -thread=1 -blocksize=63G -rw=randwrite -iodepth=32 -numjobs=1 -runtime=1200 -time_based=1
sleep 10
run

function run(){
	blockarray=(1k 4k 8k 16k 32k 64k 128k 1024k)
	rwarray=(write)  ## randread randwrite
	dparray=(32)
	sizearray=(63G)
	enginearray=(libaio)
	countarray=(1)
	# count(1)
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
							time fio -output=/home/hsu/Desktop/fio_result/${blockarray[a]}_${rwarray[b]}_${dparray[c]}_${sizearray[d]}_${enginearray[e]}_${countarray[f]} -name=test -filename=/dev/sda -ioengine=${enginearray[e]} -size=${sizearray[d]} -direct=1 -thread=1 -blocksize=${blockarray[a]} -rw=${rwarray[b]} -iodepth=${dparray[c]} -numjobs=1 -runtime=60 -time_based=1						
							sleep 10
							time fio -output=/home/hsu/Desktop/fio_result/4k_randwrite_32_63G_libaio_${countarray[f]} -name=test -filename=/dev/sda -ioengine=libaio -size=63G -direct=1 -thread=1 -blocksize=63G -rw=randwrite -iodepth=32 -numjobs=1 -runtime=600 -time_based=1
							#rm -rf /media/hsu/test${countarray[f]}
							#sleep 10
						done
					done
				done
			done
		done
	done 
}
	
##############################################################################################################
# function 4K_randwrite(min):
# 	blockarray=(4k)
# 	rwarray=(randwrite)  ## randread randwrite
# 	dparray=(32)
# 	sizearray=(63G)
# 	enginearray=(libaio)
# 	countarray=(1)
	
# 	for i in {0..10}
# 	do 
# 		#fio -output=/home/luopan/${blockarray[a]}_${rwarray[b]}_${dparray[c]}_${sizearray[d]}_${enginearray[e]} -name=${rwarray[b]} -filename=/dev/sdb -ioengine=${enginearray[e]} -size=${sizearray[d]} -direct=1 -thread=1  -blocksize=${blockarray[a]} -rw=${rwarray[b]} -iodepth=${dparray[c]} -numjobs=1
# 		time fio -output=/home/hsu/Desktop/fio_result/${blockarray[0]}_${rwarray[0]}_${dparray[0]}_${sizearray[0]}_${enginearray[0]}_${countarray[0]} -name=test -filename=/dev/sda -ioengine=${enginearray[0]} -size=${sizearray[0]} -direct=1 -thread=1 -blocksize=${blockarray[0]} -rw=${rwarray[0]} -iodepth=${dparray[0]} -numjobs=1 -runtime=$min						
# 		echo $i
# 		sleep 10
# 		# rm -rf /media/hsu/test${countarray[f]}
# 		#sleep 10
# 	done
