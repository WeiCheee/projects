#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import platform
import re
import shutil
import struct
import time
from sys import version_info
import glob
import linecache

def get_current_time():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "[%s.%03d]" % (data_head, data_secs)
    return time_stamp

def MsgOut(Sstr):
    print (get_current_time()+" "+Sstr)
    return

def catch_en():
    with open('DriveInfo.txt','rb') as f:
        print("txt file open")
        text = linecache.getline('DriveInfo.txt',86)
        print(text)
        if (text.find("not") != -1):  ###not enable->delete
            print("not enable")
            f.close()
            os.remove('DriveInfo.txt')
        else:                        ###enable stop
            print("enable")
            os.system("pause")

## change all files to 777 start
Sstr = "find ./ -type f -exec chmod 777 {} \;"
os.system(Sstr)
## change all files to 777 end
i = 0
while (i<10):
    p = os.system("hdparm --security-unlock 'zbtest' /dev/sdc")
    p = os.system("hdparm --security-set-pass 'zbtest' /dev/sdc")
    print("loop:%s"%i)
    p = os.system("hdparm --security-erase 'zbtest' /dev/sdc")
    p = os.system("hdparm -I /dev/sdc > DriveInfo.txt")
    catch_en()
    i = i+1
    





