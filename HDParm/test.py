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



def searchfile():
    local_dir = os.getcwd() ##get目前的目錄資料夾
    print("local_dir:%s"%local_dir) 
    curr_load = os.chdir("%s\\loadfile\\"%(local_dir)) ##修改當前目錄
    curr_load = os.getcwd()  ##看修改後路徑
    print("curr_load:%s"%curr_load)
    files_grab = [] ##抓到的檔案
    items = os.listdir(".") ##當前目錄的所有
    print('items:%s'%items)
    for files in items:
        if files.endswith(".txt"): ##結尾為txt的檔案
            files_grab.extend(glob.glob(files))
    print(files_grab)
    
    return files_grab

def catch_en():
    tar_file = searchfile()
    print("11111111111111111111111111")
    print(tar_file)
    input()
    try:
        with open(tar_file[0],'rb') as f:
            print("txt file open")
            catch_line = []
            text1 = linecache.getline(tar_file[0],2)
            text2 = linecache.getline(tar_file[0],3)
            print(text1)
            print(text2)
            if (text1.find("Admin") and text2.find("Host") != -1):  ###not enable(覆蓋檔案)
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

# security_type{
#     "enabled": enabled,
#     "upported": upported,
# 	"locked": locked,
# 	"frozen": frozen,
# 	"expired": expired,
#     "supported": supported,
# }
# return security_type

catch_en()
## change all files to 777 start
Sstr = "find ./ -type f -exec chmod 777 {} \;"
os.system(Sstr)
## change all files to 777 end
# i = 0
# while (i<10):
#     print("loop:%s"%i)

# i = i+1
get_current_time()    








