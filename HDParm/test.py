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

def catch_en():
    local_dir = os.getcwd() ##get目前的目錄資料夾
    print("local_dir:%s"%local_dir) 
    files_grab = [] ##抓到的檔案
    items = os.listdir(".") ##當前目錄的所有
    print('items:%s'%items)
    for files in items:
        if files.endswith(".txt"): ##結尾為txt的檔案
            files_grab.extend(glob.glob(files))
    print(files_grab)

    try:
        with open(files_grab[0],'rb') as f:
            print("txt file open")
            catch_line = []
            text = linecache.getline(files_grab[0],2)
            print(text)
            if (text.find("Admin") != -1):  ###not enable(覆蓋檔案)
                print("get word!")
            else:                         ###enable(停)
                print("not found")
    except:
        print("faile open file")

def get_current_time():
    ct = time.time() ##總秒數
    local_time = time.localtime(ct) ##struct的時間
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time) ##轉成需要的格式
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "[%s.%03d]" % (data_head, data_secs)
    return time_stamp

def MsgOut(Sstr):
    print (get_current_time()+" "+Sstr)
    return

## change all files to 777 start
Sstr = "find ./ -type f -exec chmod 777 {} \;"
os.system(Sstr)
## change all files to 777 end
# i = 0
# while (i<10):
#     print("loop:%s"%i)
catch_en()
# i = i+1
get_current_time()    








