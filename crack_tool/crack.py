import tkinter as tk
import tkinter.messagebox as messagebox
import subprocess
import win32api
import win32con
import time

kms:{
    win10_64_pro:"",
    win10_64_edu:"",
    win
}

cmd:{
    exe_path:"%SystemRoot%\system32\WindowsPowerShell\\v1.0\powershell.exe",
    process:{
        clean_sec_key:"slmgr.vbs -upk",
        kms_key:"slmgr.vbs -ipk"
        sever_ip:"slmgr.vbs -skms kms.cangshui.net",
        ato:"slmgr.vbs -ato",
        vbs:"slmgr.vbs –dlv"
    },

}


def aa(bb)):
    cmd.process.kms_key = cmd.process.kms_key + " " + kms[bb]


def win10_64_pro(Process):
    subprocess.call("%s %s"%(cmd.exe_path,cmd.process[]), shell=True)
    time.sleep(3)
    win32api.keybd_event(13,0,0,0)
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
    

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