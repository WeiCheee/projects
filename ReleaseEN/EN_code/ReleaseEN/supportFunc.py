import xlrd
import glob
import datetime
import json
import os
import shutil
from os.path import isfile,isdir
import time
import sys

def ReadXLS():
    # 取得副檔名為 xls 的檔案
    xls = glob.glob(r".\\ENTool\_FRF\*.xls")
    workbook = xlrd.open_workbook(xls[0])
    booksheet = workbook.sheet_by_index(0)

    data = []
    context = booksheet.cell_value(8,1)
    model_number = booksheet.cell_value(23,2)
    data.append(context)
    data.append(model_number)
    # data = {'context':context,'modelNumber':model_number}
    return data


def ReadTXT():
    # 查找txt檔案
    massage_txt = glob.glob(r".\\ENTool\*.txt")
    lines = []
    with open(massage_txt[0],'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            line = line.strip('\n')
            if not line:
                break
            if(line.find("Check SUM") != -1):
                if(len(lines) == 2):
                    lines.insert(1,"")
                spstr = line.split(" = ")
                lines.append(spstr[-1])
            else:
                lines.append(line)
    return lines
            
def SetTime():
    time = datetime.datetime.now()
    date = datetime.date.today()
    weekday = date.weekday()
    add_day = 0

    # 超過5點
    if(time.hour >= 17):
        if(weekday == 3):
            add_day = 2
        elif(weekday == 4):
            add_day = 1
        return date + datetime.timedelta(days = 2 + add_day)
    else:
        if(weekday == 4):
            add_day = 2
        elif(weekday == 5):
            add_day = 1
        return date + datetime.timedelta(days = 1 + add_day)
    


def ReadJson():
    with open('Parameters.json') as json_file:
        data = json.load(json_file)
    return data



def RunWinRAR():
    now_dir = os.getcwd()
    os.chdir("%s\\ENTool"%(now_dir))
    os.system("%s\\ENTool\\EN_helper_for_Brian.exe"%(now_dir))
    os.chdir(now_dir)

def CheckRAR():
    while(True):
        rar = glob.glob(".\ENTool\_rar\*")
        print(rar)
        if(len(rar) >= 4):
            break
        else:
            time.sleep(2)
    return


def CheckXLS():
    while(True):
        xls = glob.glob(".\Data_Put_Here\*.xls")
        if(len(xls) != 0):
            break
        else:
            time.sleep(2)
    return


def ReadRAR():
    now_dir = os.getcwd()
    _rar_Path = "%s\\ENTool\_rar\\"%(now_dir)
    rar = os.listdir(r".\ENTool\_rar")
    RAR = {
        "rar":"",
        "_bin":"",
        "_dat":"",
        "_FRF":""
    }
    for i in range(0,len(rar)):
        if(rar[i].find("_") == -1):
            RAR["rar"] = _rar_Path + rar[i]
        else:
            if(rar[i].find("_bin") != -1):   
                RAR["bin"] = _rar_Path + rar[i]
            elif(rar[i].find("_dat") != -1):
                RAR["dat"] = _rar_Path + rar[i]
            elif(rar[i].find("_FRF") != -1):
                RAR["FRF"] = _rar_Path + rar[i]
    return(RAR)


def MoveFile(FW_Name):
    now_dir = os.getcwd()
    
    message_txt = glob.glob(".\ENTool\*.txt")
    if(len(message_txt) != 0):
        os.remove(message_txt[0])

    
    DPH_xls = glob.glob(".\Data_Put_Here\*.xls")
    FRF_old_xls = glob.glob(".\ENTool\_FRF\*.xls")
    FRF_new_xls = ".\ENTool\_FRF\%s_FRF.xls"%(FW_Name)
    # copy xls to FRF file
    if(len(FRF_old_xls) != 0):
        os.remove(FRF_old_xls[0])
    shutil.move(DPH_xls[0],FRF_new_xls)

    DPH_code = glob.glob("%s\Data_Put_Here\*"%(now_dir))
    DPH_code_newName = "%s\Data_Put_Here\%s"%(now_dir,FW_Name)
    AutoRun_new_code = "%s\ENTool\FWReleaseTool\AutoRun\\"%(now_dir)
    AutoRun_old_code = glob.glob("%s\ENTool\FWReleaseTool\AutoRun\*"%(now_dir))

    sChkSum_exe = "%s\ENTool\sChkSum.exe"%(now_dir)
    
    if(len(AutoRun_old_code) != 0):
        garbage_num = len(os.listdir("%s\ENTool\Garbage\\"%(now_dir)))
        shutil.move(AutoRun_old_code[0],"%s\ENTool\Garbage\%s"%(now_dir,garbage_num))
        # shutil.rmtree(AutoRun_old_code[0])
    for f in DPH_code:
        if isdir(f):
            os.rename(f, DPH_code_newName)
            shutil.move(DPH_code_newName,AutoRun_new_code)
            shutil.copy(sChkSum_exe,"%s\%s\sChkSum.exe"%(AutoRun_new_code,(os.listdir(AutoRun_new_code))[0]))
    FRF_old_code = (glob.glob(".\ENTool\_FRF\*.xls"))[0]
    FRF_new_code = ".\ENTool\_FRF\%s.xls"%(FW_Name)


def checkFwLastName(FW_Name):
    str1 = FW_Name
    if(FW_Name[-1] == "0"):
        str1 = str1[:-1]
    return str1

def CheckAndAddFwLastName(FW_Name):
    if(len(FW_Name) == 7):
        return "%s0"%(FW_Name)
    else:
        return FW_Name

def ReadCodeFW():
    try:
        FW_Name = os.listdir("./Data_Put_Here")
        return FW_Name[0]
    except:
        print("Please put FW code into \'Data_Put_Here\' file")
        sys.exit()

