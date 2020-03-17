import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QComboBox, QApplication

from PyQt5.QtCore import  QEventLoop, QTimer
from PyQt5 import QtCore, QtGui
# from Ui_ControlBoard import Ui_MainWindow

class ComboxDemo(QWidget):
    def __init__(self):
        super().__init__()
        # 设置标题
        self.setWindowTitle('Windows Crash')
        # 设置初始界面大小
        self.resize(300, 200)
        # 实例化QComBox对象
        self.cb = QComboBox(self)
        self.cb.move(30, 20)
        
        # self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        # self.progressBar.setGeometry(QtCore.QRect(220, 180, 141, 16))
        # self.progressBar.setProperty("value", 24)
        # self.progressBar.setObjectName("progressBar")
        # 单个添加条目
        # self.cb.addItem('C')
        # self.cb.addItem('C++')
        # self.cb.addItem('Python')
        # 多个添加条目
        self.cb.addItems(['Win 10 pro', 'Win 10 pro N', 'Win 10 edu', 'Win 8.1 pro', 'Win 8 pro', 'Win 7 pro'])

        # 信号
        self.cb.currentIndexChanged[str].connect(self.print_value) # 条目发生改变，发射信号，传递条目内容
        self.cb.currentIndexChanged[int].connect(self.print_value)  # 条目发生改变，发射信号，传递条目索引
        self.cb.highlighted[str].connect(self.print_value)  # 在下拉列表中，鼠标移动到某个条目时发出信号，传递条目内容
        self.cb.highlighted[int].connect(self.print_value)  # 在下拉列表中，鼠标移动到某个条目时发出信号，传递条目索引

    def print_value(self, i):
        print(i)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    comboxDemo = ComboxDemo()
    comboxDemo.show()
    sys.exit(app.exec_())