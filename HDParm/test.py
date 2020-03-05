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
    print("hello")
    types = ('*.txt')
    files_grab = []
    for files in types:
        files_grab.extend(glob.glob(files))
    print(files_grab)

    # files_grab = [glob.glob(files) for files in ['*.text']]
    # print(files_grab)

    with open(files_grab[1],'rb') as f:
        print("txt file can open")
        catch_line = []
        text = linecache.getline(files_grab[1],86)
        print(text)
        if (text.find("not") != -1):  ###not enable(覆蓋檔案)
            print("not enable")
            # return 0
        else:                         ###enable(停)
            print("enable")

catch_en()
# if(catch_en() == 0):
#     os.system("pause")
# else:






