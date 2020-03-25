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
        # self.procces_stop = procces_stop
        self.selected = '--version--' # 需要給selected物件預設值
        self.setupUi(self)
        self.t = threading.Thread.__init__(self)
        # self.thread_num = thread_num
        # self.call_event(self)
        self.stopped = False
        self.timeout = 10

if __name__ == '__main__':

    app = QApplication(sys.argv)
    comboxDemo = Mainwindows()
    comboxDemo.show()
    sys.exit(app.exec_())

    #print("111111")