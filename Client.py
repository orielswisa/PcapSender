from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import socket
import threading
import time




class Worker(QRunnable):
    def __init__(self,skt,messagelistWidget):
        super(Worker, self).__init__()
        self.skt = skt
        self.messagelistWidget = messagelistWidget
        self.flag = True
        

    def run(self):
        print(self.skt)
        print("Thread start")
        while self.flag:
            c, addr = self.skt.recvfrom(1024)
            self.messagelistWidget.addItem("got connection",addr)
            self.messagelistWidget.addItem(c)
        print("Thread complete")

class ClientWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(ClientWin,self).__init__()
        self.setupUi(self)
        self.skt = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(280, 475)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.open_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.open_pushButton.setGeometry(QtCore.QRect(70, 180, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(12)
        self.open_pushButton.setFont(font)
        self.open_pushButton.setObjectName("open_pushButton")
        self.port_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.port_edit.setGeometry(QtCore.QRect(70, 130, 131, 31))
        self.port_edit.setObjectName("port_edit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 131, 31))
        self.label_2.setObjectName("label_2")
        self.messagelistWidget = QtWidgets.QListWidget(self.centralwidget)
        self.messagelistWidget.setGeometry(QtCore.QRect(10, 250, 256, 171))
        self.messagelistWidget.setObjectName("messagelistWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Clicked function
        self.open_pushButton.clicked.connect(self.open_port)

    def closeEvent(self, event):
        print("event")
        self.threadpool.stop()

    def open_port(self):
        try:
            self.skt.bind(('',int(self.port_edit.toPlainText())))
            self.worker = Worker(self.skt,self.messagelistWidget)
            self.threadpool.start(self.worker)   
        except:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Cannot open this port")
            self.msg.setInformativeText('Please enter valid port')
            self.msg.setWindowTitle("Error")
            self.msg.exec_()
        
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Pcap listener"))
        self.open_pushButton.setText(_translate("MainWindow", "Open port"))
        self.label_2.setText(_translate("MainWindow", "Enter port number:"))

    def stop(self): # called when X in main window pressed
        print("Close all theards")
        self.threadpool.stop()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    demo = ClientWin()
    demo.show() 

    # MainWindow = QtWidgets.QMainWindow()
    # ui = ClientWin()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    sys.exit(app.exec_())
