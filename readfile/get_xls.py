import os
import glob
import xlrd 
import json
from os import listdir
from os.path import isfile, isdir, join
from types import *
import filetype
import time 
from tabulate import tabulate
import pandas as pd
import win32com.client as win32
# from GrabzIt import GrabzItClient
write_to_txt = 1
write_to_mail = 0
import matplotlib.pyplot as plt
import numpy as np

def read_excel(path, number):
    row = number+1
    colum = 10
    arr = []
    inside = []
    try:
        with xlrd.open_workbook(path) as f:
            sheet1 = f.sheets()[0]
            for i in range(0, row):
                for j in range(0, colum):
                    cell_value = sheet1.cell_value(i,j)
                    if(i > 0 and j == 0): ###date
                        time_tuple1 = xlrd.xldate_as_tuple(cell_value,f.datemode)
                        time_tuple2 = (0, 0, 0)
                        time_tuple = time_tuple1 + time_tuple2
                        print(time_tuple)
                        add_day = time.strftime("%Y/%m/%d", time_tuple)
                        print(add_day)
                        inside.append(add_day)
                    else:
                        inside.append(cell_value)
                arr.append(inside)
                inside = [] 
    except:
        print("read file Error!!!")
    return arr 

def getinfo(number):
    datapath = "C:\\Users\\test\\Desktop\\projects\\readfile\\datafile\\"
    types = ['.txt', '.dat', '.xlsm'] ###grab file type###
    filename = "CV8_FW_Relation"
    path = os.listdir(datapath) 
    print(path)
    
    for getfile in path:
        getNamebefore = getfile
        getName = os.path.splitext(getfile)[0]
        if (getName == filename):
            returnPath = datapath + getNamebefore
        else:
            print("get file path Error!!")
    ###----------get 2D list data------------
    arr_data = read_excel(returnPath, number)
    html_table = tabulate(arr_data, tablefmt='html')
    html_table = str(html_table)
    print(html_table)
    print(type(html_table))  
    print("--------------------------------------------------------\n")   
    print("---------------arr_data : ------------------------\n", arr_data)
    

    if(write_to_mail):
        send_after = tansfer_table(returnPath, number)
        if(send_after):
            return 1
        else:
            return 0

    if(write_to_txt):
        try:    
            with open('test_Info.txt', 'w+', encoding="utf-8") as f:
                f.write("test files:\n")
                f.write(returnPath + '\n') 
                f.write("info:\n")
                for items in arr_data:
                    f.write(str(items))
                    f.write("\n")
                f.write("html table : \n")
                f.write(html_table)
            f.close()

            with open('test_table.txt', 'w+', encoding="utf-8") as f:
                f.write(html_table)
            f.close()               
        except:
            print("write file Error!!!")
            return 0
    return 1

def tansfer_table(path, num):
    df = pd.read_excel(path, index_col=False, nrows = num,  usecols = "A:L")
    html_table = df.to_html()  
    print(html_table)
    outlook = win32.gencache.EnsureDispatch('Outlook.Application')
    mail_item = outlook.CreateItem(0)
    mail_item.To = 'Charles.Hsu@ssstc.com'
    mail_item.Attachments.Add(Source=path)
    # body = "<h1>Dear ABC</h1>This is the Table <br><br>   "+html_table+"   <br><br> this is image <br><br><img src=ownload.png><br><br>Thanks"
    body = html_table
    mail_item.HTMLBody = (body)
    try:
        mail_item.Send()
    except:
        print("send mail fail")
        return 0
    return 1


if __name__ == '__main__':
    number = 8
    success = getinfo(number)
    if(success):
        print("\nprocess succed")
        os.system("pause")
    else: 
        print("\nprocess fail")

