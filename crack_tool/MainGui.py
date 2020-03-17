import sys
from GUI2 import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QApplication

class Mainwindows(QMainWindow, Ui_MainWindow): 
    def __init__(self, parent=None):
        super(Mainwindows, self).__init__(parent)
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    comboxDemo = Mainwindows()
    comboxDemo.show()
    sys.exit(app.exec_())