
# -------------------------------------------------------------------------------------------------------------------------
fio -output=/home/hsu/Desktop/fio_result/4k_randwrite_32_63G_libaio_1 -name=test -filename=/dev/sda -ioengine=libaio -size=63G -direct=1 -thread=1 -blocksize=63G -rw=randwrite -iodepth=32 -numjobs=1 -runtime=1200 -time_based=1
sleep 10


function script(){
    block=$1
    rw=$2
    runtime=$3

    fio -output=/home/hsu/Desktop/fio_result/${block}_${rw}_${runtime} -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=${block} -rw=${rw} -iodepth=32 -numjobs=1 -runtime=${runtime} -time_based=1
}

# step 1 ----------------------------------------------
fio -output=/home/hsu/Desktop/fio_result/1M_write_step1 -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=1024k -rw=write -iodepth=32 -numjobs=1 -size=63G

# step 2 ----------------------------------------------
fio -output=/home/hsu/Desktop/fio_result/4M_randwrite_step2 -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=4k -rw=randwrite -iodepth=32 -numjobs=1 -runtime=7200 -time_based=1

# step 3 ----------------------------------------------
for runtime in {8000,240}
do
    script "1k" "randwrite" $runtime
done

for runtime in {4000,240}
do
    script "4k" "randwrite" $runtime
done

for runtime in {2000,240}
do
    script "8k" "randwrite" $runtime
done

for runtime in {1000,240}
do
    script "16k" "randwrite" $runtime
done

for runtime in {500,240}
do
    script "32k" "randwrite" $runtime
done

for runtime in {250,240}
do# step 1 ----------------------------------------------
fio -output=/home/hsu/Desktop/fio_result/1M_write_step1 -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=1024k -rw=write -iodepth=32 -numjobs=1 -size=63G

# step 2 ----------------------------------------------
fio -output=/home/hsu/Desktop/fio_result/4M_randwrite_step2 -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=4k -rw=randwrite -iodepth=32 -numjobs=1 -runtime=7200 -time_based=1

# step 3 ----------------------------------------------
for runtime in {8000,240}
do
    script "1k" "randwrite" $runtime
done

for runtime in {4000,240}
do
    script "4k" "randwrite" $runtime
done

for runtime in {2000,240}
do
    script "8k" "randwrite" $runtime
done

for runtime in {1000,240}
do
    script "16k" "randwrite" $runtime
done

for runtime in {500,240}
do
    script "32k" "randwrite" $runtime
done

for runtime in {250,240}
do
    script "64k" "randwrite" $runtime
done

for runtime in {125,240}
do
    script "128k" "randwrite" $runtime
done

for runtime in {"62.5",240}
do
    script "256k" "randwrite" $runtime
done


# step 4 ----------------------------------------------
fio -output=/home/hsu/Desktop/fio_result/1M_write_step4 -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=1024k -rw=write -iodepth=32 -numjobs=1 -size=63G
fio -output=/home/hsu/Desktop/fio_result/1M_write_step4_2 -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=1024k -rw=write -iodepth=32 -numjobs=1 -size=63G

# step 5 ----------------------------------------------
for runtime in {8000,240}
do
    script "1k" "write" $runtime
done

for runtime in {4000,240}
do# step 1 ----------------------------------------------
fio -output=/home/hsu/Desktop/fio_result/1M_write_step1 -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=1024k -rw=write -iodepth=32 -numjobs=1 -size=63G

# step 2 ----------------------------------------------
fio -output=/home/hsu/Desktop/fio_result/4M_randwrite_step2 -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=4k -rw=randwrite -iodepth=32 -numjobs=1 -runtime=7200 -time_based=1

# step 3 ----------------------------------------------
for runtime in {8000,240}
do
    script "1k" "randwrite" $runtime
done

for runtime in {4000,240}
do
    script "4k" "randwrite" $runtime
done

for runtime in {2000,240}
do
    script "8k" "randwrite" $runtime
done

for runtime in {1000,240}
do
    script "16k" "randwrite" $runtime
done

for runtime in {500,240}
do
    script "32k" "randwrite" $runtime
done

for runtime in {250,240}
do
    script "64k" "randwrite" $runtime
done

for runtime in {125,240}
do
    script "128k" "randwrite" $runtime
done

for runtime in {"62.5",240}
do
    script "256k" "randwrite" $runtime
done


# step 4 ----------------------------------------------
fio -output=/home/hsu/Desktop/fio_result/1M_write_step4 -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=1024k -rw=write -iodepth=32 -numjobs=1 -size=63G
fio -output=/home/hsu/Desktop/fio_result/1M_write_step4_2 -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=1024k -rw=write -iodepth=32 -numjobs=1 -size=63G

# step 5 ----------------------------------------------
for runtime in {8000,240}
do
    script "1k" "write" $runtime
done

for runtime in {4000,240}
do# step 1 ----------------------------------------------
fio -output=/home/hsu/Desktop/fio_result/1M_write_step1 -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=1024k -rw=write -iodepth=32 -numjobs=1 -size=63G

# step 2 ----------------------------------------------
fio -output=/home/hsu/Desktop/fio_result/4M_randwrite_step2 -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=4k -rw=randwrite -iodepth=32 -numjobs=1 -runtime=7200 -time_based=1

# step 3 ----------------------------------------------
for runtime in {8000,240}
do
    script "1k" "randwrite" $runtime
done

for runtime in {4000,240}
do
    script "4k" "randwrite" $runtime
done

for runtime in {2000,240}
do
    script "8k" "randwrite" $runtime
done

for runtime in {1000,240}
do
    script "16k" "randwrite" $runtime
done

for runtime in {500,240}
do
    script "32k" "randwrite" $runtime
done

for runtime in {250,240}
do
    script "64k" "randwrite" $runtime
done

for runtime in {125,240}
do
    script "128k" "randwrite" $runtime
done

for runtime in {"62.5",240}
do
    script "256k" "randwrite" $runtime
done


# step 4 ----------------------------------------------
fio -output=/home/hsu/Desktop/fio_result/1M_write_step4 -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=1024k -rw=write -iodepth=32 -numjobs=1 -size=63G
fio -output=/home/hsu/Desktop/fio_result/1M_write_step4_2 -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=1024k -rw=write -iodepth=32 -numjobs=1 -size=63G

# step 5 ----------------------------------------------
for runtime in {8000,240}
do
    script "1k" "write" $runtime
done

for runtime in {4000,240}
do
    script "4k" "write" $runtime
done

for runtime in {2000,240}
do
    script "8k" "write" $runtime
done

for runtime in {1000,240}
do
    script "16k" "write" $runtime
done

for runtime in {500,240}
do
    script "32k" "write" $runtime
done

for runtime in {250,240}
do
    script "64k" "write" $runtime
done

for runtime in {125,240}
do
    script "128k" "write" $runtime
done

for runtime in {"62.5",240}
do
    script "256k" "write" $runtime
done



sleep 60
    script "4k" "write" $runtime
done

for runtime in {2000,240}
do
    script "8k" "write" $runtime
done

for runtime in {1000,240}
do
    script "16k" "write" $runtime
done

for runtime in {500,240}
do
    script "32k" "write" $runtime
done

for runtime in {250,240}
do
    script "64k" "write" $runtime
done

for runtime in {125,240}
do
    script "128k" "write" $runtime
done

for runtime in {"62.5",240}
do
    script "256k" "write" $runtime
done



sleep 60

for runtime in {2000,240}
do
    script "8k" "write" $runtime
done

for runtime in {1000,240}
do
    script "16k" "write" $runtime
done

for runtime in {500,240}
do
    script "32k" "write" $runtime
done

for runtime in {250,240}
do
    script "64k" "write" $runtime
done

for runtime in {125,240}
do
    script "128k" "write" $runtime
done

for runtime in {"62.5",240}
do
    script "256k" "write" $runtime
done



sleep 60
    script "64k" "randwrite" $runtime
done

for runtime in {125,240}
do
    script "128k" "randwrite" $runtime
done

for runtime in {"62.5",240}
do
    script "256k" "randwrite" $runtime
done


# step 4 ----------------------------------------------
fio -output=/home/hsu/Desktop/fio_result/1M_write_step4 -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=1024k -rw=write -iodepth=32 -numjobs=1 -size=63G
fio -output=/home/hsu/Desktop/fio_result/1M_write_step4_2 -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=1024k -rw=write -iodepth=32 -numjobs=1 -size=63G

# step 5 ----------------------------------------------
for runtime in {8000,240}
do
    script "1k" "write" $runtime
done

for runtime in {4000,240}
do
    script "4k" "write" $runtime
done

for runtime in {2000,240}
do
    script "8k" "write" $runtime
done

for runtime in {1000,240}
do
    script "16k" "write" $runtime
done

for runtime in {500,240}
do
    script "32k" "write" $runtime
done

for runtime in {250,240}
do
    script "64k" "write" $runtime
done

for runtime in {125,240}
do
    script "128k" "write" $runtime
done

for runtime in {"62.5",240}
do
    script "256k" "write" $runtime
done



sleep 60