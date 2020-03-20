import tkinter as tk
import tkinter.messagebox as messagebox
import subprocess
import win32api
import win32con
import time
import os

kms = {
    '--version--':"NULL",
    'win10 x64 pro':"W269N-WFGWX-YVC9B-4J6C9-T83GX",
    'win10 x64 pro_N':"MH37W-N47XK-V7XM9-C7227-GCQG9",
    'win10 x64 edu':"NW6C2-QMPVW-D7KKK-3GKT6-VCFB2",
    'win8.1 pro':"GCRJD-8NW9H-F2CDX-CCM8D-9D6T9",
    'win8 pro':"NG4HW-VH26C-733KW-K6F98-J8CK4",
    'win7 pro':"FJ82H-XT6CR-J8D7P-XQJJ2-GPDD4",
}

cmd = {
    'exe_path':"%SystemRoot%\system32\WindowsPowerShell\\v1.0\powershell.exe",
    'process':{
        'clean_sec_key':"slmgr.vbs -upk",
        'kms_ins':"slmgr.vbs -ipk",
        'sever_ip':"slmgr.vbs -skms kms.cangshui.net",
        'ato':"slmgr.vbs -ato",
        'vbs':"slmgr.vbs –dlv",
    },

}

def kms_key(ver, cmd):
    # origin_str = cmd['process']['kms_ins']
    cmd_kms_ins = cmd['process']['kms_ins'].split(" ",2)
    print(cmd_kms_ins)
    cmd_kms_ins = cmd_kms_ins[0] + " " + cmd_kms_ins[1]
    print(cmd_kms_ins)
    cmd['process']['kms_ins'] = cmd_kms_ins + " " + kms[ver]
    print(cmd['process']['kms_ins'])
   
    return 1

def windows_crash(ver, cmd):
    success = kms_key(ver,cmd)
    # print(success)
    if(success):
        # for item in cmd['process']:
        #     p = subprocess.call("%s %s"%(cmd['exe_path'],cmd['process'][item]) , shell=True)
        #     time.sleep(3)
        #     win32api.keybd_event(13,0,0,0)
        #     win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
        #     time.sleep(1)
        printcmd()
    else:
        print("Error input")

def printcmd():
    print("--------------------------------------------------\n")
    for item in cmd['process']:
        print("%s %s"%(cmd['exe_path'],cmd['process'][item]))
    # while True:
    #     print("stop")
        # time.sleep(10)
  
def procces_stop():
    subprocess.call("pause", shell=True)
    # print ("iii")


#print("111111")