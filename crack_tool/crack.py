import tkinter as tk
import tkinter.messagebox as messagebox
import subprocess
import win32api
import win32con
import time

kms = {
    'win10_64_pro':"W269N-WFGWX-YVC9B-4J6C9-T83GX",
    'win10_64_pro_N':"MH37W-N47XK-V7XM9-C7227-GCQG9",
    'win10_64_edu':"NW6C2-QMPVW-D7KKK-3GKT6-VCFB2",
    'win81_pro':"GCRJD-8NW9H-F2CDX-CCM8D-9D6T9",
    'win8_pro':"NG4HW-VH26C-733KW-K6F98-J8CK4",
    'win7_pro':"FJ82H-XT6CR-J8D7P-XQJJ2-GPDD4",
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
    cmd['process']['kms_ins'] = cmd['process']['kms_ins'] + " " + kms[ver]
    return 1

def windows_crash(ver, cmd):
    success = kms_key(ver,cmd)
    if(success):
        for item in cmd['process']:
            subprocess.call("%s %s"%(cmd['exe_path'],cmd['process'][item]) , shell=True)
            time.sleep(3)
            win32api.keybd_event(13,0,0,0)
            win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
            time.sleep(1)
    else:
        print("Error input")

ver = input("choose version:")
windows_crash(ver, cmd)

# for i in kms.keys():
#     print(i)
# print(len(list(kms.keys())))
# print(list(kms.keys())[0])

# def HelloWorldMsgBox():
#     print('hello world')
#     messagebox.showinfo("Hello World Application", "Hello World!") #呼叫hello world的訊息框

# root = tk.Tk()
# # root.minsize(300,100)
# root.geometry("500x300")
# root.title('Application')

# buttonHelloWorld = tk.Button(root, text='Active', width=25, height=5, command=HelloWorldMsgBox)
# buttonHelloWorld.pack() #按下去啟動上面定義好的HelloWorldMsgBox方法

# buttonClose = tk.Button(root, text='Close', width=25, command=root.destroy)
# buttonClose.pack() #按下去啟動root.destroy，也就是關閉視窗
# root.mainloop()

