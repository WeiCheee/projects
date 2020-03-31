
# -------------------------------------------------------------------------------------------------------------------------
# fio -output=/home/hsu/Desktop/fio_result/4k_randwrite_32_63G_libaio_1 -name=test -filename=/dev/sdd -ioengine=libaio -size=63G -direct=1 -thread=1 -blocksize=63G -rw=randwrite -iodepth=32 -numjobs=1 -runtime=1200 -time_based=1
# sleep 10
# fio -output=/home/hsu/Desktop/fio_result/4M_randwrite_steptest -name=test -filename=/dev/sdd -ioengine=libaio -direct=1 -thread=1 -blocksize=4k -rw=randwrite -iodepth=32 -numjobs=1 -runtime=60 -time_based=1 -log_avg_msec=1000 -write_bw_log=/home/hsu/Desktop/fio_result/testlog1
# fio -output=/home/hsu/Desktop/fio_result/4M_randwrite_steptest -name=test -filename=/dev/sdd -ioengine=libaio -direct=1 -thread=1 -blocksize=4k -rw=randwrite -iodepth=32 -numjobs=1 -runtime=60 -time_based=1 -log_avg_msec=1000 -write_bw_log=/home/hsu/Desktop/fio_result/testlog2
function script(){
    block=$1
    rw=$2
    runtime=$3
    step=$4 
    fio -output=/home/hsu/Desktop/fio_result/${block}_${rw}_${runtime}_${step} -name=test -filename=/dev/sdd -ioengine=libaio -direct=1 -thread=1 -blocksize=${block} -rw=${rw} -iodepth=32 -numjobs=1 -runtime=${runtime} -time_based=1 -log_avg_msec=1000 -write_bw_log=/home/hsu/Desktop/fio_result/log_${block}_${rw}_${runtime}_${step}
}


# step 1 ----------------------------------------------
fio -output=/home/hsu/Desktop/fio_result/1M_write_step1 -name=test -filename=/dev/sdd -ioengine=libaio -direct=1 -thread=1 -blocksize=1024k -rw=write -iodepth=32 -numjobs=1 -size=63G
sleep 10
# step 2 ----------------------------------------------
fio -output=/home/hsu/Desktop/fio_result/4k_randwrite_step2 -name=test -filename=/dev/sdd -ioengine=libaio -direct=1 -thread=1 -blocksize=4k -rw=randwrite -iodepth=32 -numjobs=1 -runtime=7200 -time_based=1 -log_avg_msec=1000 -write_bw_log=/home/hsu/Desktop/fio_result/log_step2
sleep 10
# step 3 ----------------------------------------------

for runtime in {8000,240}
do
    script "1k" "randwrite" $runtime "step3"
done

for runtime in {4000,240}
do
    script "4k" "randwrite" $runtime "step3"
done

for runtime in {2000,240}
do
    script "8k" "randwrite" $runtime "step3"
done

for runtime in {1000,240}
do
    script "16k" "randwrite" $runtime "step3"
done

for runtime in {500,240}
do
    script "32k" "randwrite" $runtime "step3"
done

for runtime in {250,240}
do
    script "64k" "randwrite" $runtime "step3"
done

for runtime in {125,240}
do
    script "128k" "randwrite" $runtime "step3"
done

for runtime in {"62.5",240}
do
    script "1024k" "randwrite" $runtime "step3"
done
sleep 10
# step 4 ----------------------------------------------
fio -output=/home/hsu/Desktop/fio_result/1M_write_step4 -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=1024k -rw=write -iodepth=32 -numjobs=1 -size=63G
fio -output=/home/hsu/Desktop/fio_result/1M_write_step4_2 -name=test -filename=/dev/sda -ioengine=libaio -direct=1 -thread=1 -blocksize=1024k -rw=write -iodepth=32 -numjobs=1 -size=63G
sleep 10
# # step 5 ----------------------------------------------
for runtime in {8000,240}
do
    script "1k" "write" $runtime "step5"
done

for runtime in {4000,240}
do
    script "4k" "write" $runtime "step5"
done

for runtime in {2000,240}
do
    script "8k" "write" $runtime "step5"
done

for runtime in {1000,240}
do
    script "16k" "write" $runtime "step5"
done

for runtime in {500,240}
do
    script "32k" "write" $runtime "step5"
done

for runtime in {250,240}
do
    script "64k" "write" $runtime "step5"
done

for runtime in {125,240}
do
    script "128k" "write" $runtime "step5"
done

for runtime in {"62.5",240}
do
    script "1024k" "write" $runtime "step5"
done



