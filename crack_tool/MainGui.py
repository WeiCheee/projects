import sys
from GUI2 import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QApplication
from crack import *
import threading

class Mainwindows(QMainWindow, Ui_MainWindow): 
    def __init__(self, parent=None):
        super(Mainwindows, self).__init__(parent)
        self.kms = kms
        self.cmd = cmd
        self.windows_crash = windows_crash
        self.procces_stop = procces_stop
        self.selected = '--version--' # 需要給selected物件預設值
        # self.windows_crash('win10_64_pro',self.cmd)
        # print(self.windows_crash)
        # self.print_value(self)
        self.setupUi(self)
        self.t = threading.Thread.__init__(self)
        # self.call_event(self)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    comboxDemo = Mainwindows()
    comboxDemo.show()
    sys.exit(app.exec_())
    #print("111111")